from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from books.models import Book

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='subcategories', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def clean(self):
        if self.parent and self.parent.parent:
            raise ValidationError(
                'Only subcategories of second level allowed. You can not create subcategory of subcategory'
            )

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug, 'pk': self.pk})

    def __str__(self):
       return self.name

    def get_all_books(self):
        in_categories = list(self.subcategories.all().values_list('pk', flat=True))
        in_categories.append(self.pk)
        return Book.objects.filter(categories__in=in_categories)
