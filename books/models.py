from django.db import models
from books.validators import ISBNValidator
from django.urls import reverse
from django.utils.text import slugify


class Book(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    categories = models.ManyToManyField('categories.Category', related_name='books')
    isbn = models.CharField(max_length=13, validators=[ISBNValidator])

    class Meta:
        verbose_name_plural = 'books'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book', kwargs={'slug': self.slug, 'pk': self.pk})
