from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from categories.models import Category


class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['parent'].queryset = form.fields['parent'].queryset.filter(parent__isnull=True)
        return form

class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['parent'].queryset = form.fields['parent'].queryset.filter(parent__isnull=True)
        return form

class CategoryList(ListView):
    model = Category
    paginate_by = 5
    queryset = Category.objects.filter(parent__isnull=True)

class CategoryDetailView(DetailView):
    queryset = Category.objects.all()