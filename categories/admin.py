from django.contrib import admin
from django.urls import reverse
from django.utils.encoding import force_text
from categories.models import Category
from django.utils.safestring import mark_safe

class SubcategoriesListFilter(admin.SimpleListFilter):
    title = 'What to list?'
    template = "admin/subcategories_filter.html"

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'subcategories'
    subcategory_lookup = 'sub'

    def lookups(self, request, model_admin):
        return (
            (self.subcategory_lookup, 'Subcategories'),
        )

    def choices(self, changelist):
        yield {
            'selected': self.value() is None,
            'query_string': changelist.get_query_string({}, [self.parameter_name]),
            'display': 'Categories',
        }
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == force_text(lookup),
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        if self.value() == 'sub':
            return queryset.filter(parent__isnull=False)
        if self.value() is None:
            return queryset.filter(parent__isnull=True)


class SubCategoryInline(admin.TabularInline):
    model = Category



class CategoryAdmin(admin.ModelAdmin):
    list_filter = (SubcategoriesListFilter, )
    inlines = [
        SubCategoryInline,
    ]


    def subcategory_display(self, obj):
        subcategories_string = ", ".join([
            subcategory.name for subcategory in obj.subcategories.all()[:7]
        ])
        url = reverse('admin:categories_category_changelist')
        sub_param = SubcategoriesListFilter.parameter_name
        sub_value = SubcategoriesListFilter.subcategory_lookup
        q_string = f'parent__id__exact={obj.pk}&{sub_param}={sub_value}'
        return mark_safe(f'<a href="{url}?{q_string}">{subcategories_string}</a>')

    subcategory_display.short_description = "Subcategories"

    list_display = ('name', 'slug', 'subcategory_display',)
    list_select_related = (
        'parent',
    )

    def get_list_display(self, request):
        subcategories = request.GET.get(SubcategoriesListFilter.parameter_name)
        if subcategories:
            list_display = ('name', 'slug')
        else:
            list_display = self.list_display
        return list_display

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent":
            kwargs["queryset"] = Category.objects.filter(parent__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category, CategoryAdmin)