from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from books.models import Book


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'description', 'isbn', 'categories']


class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'description', 'isbn', 'categories']


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('category-list')


class BookDetailView(DetailView):
    queryset = Book.objects.all()
