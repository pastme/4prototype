from django.urls import path
from categories.views import CategoryList, CategoryDetailView, CategoryCreate, CategoryUpdate

urlpatterns = [
    path('', CategoryList.as_view(), name='category-list'),
    path('category/<slug:slug>-<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('category/add/', CategoryCreate.as_view(), name='category-add'),
    path('category/update/<int:pk>/', CategoryUpdate.as_view(), name='category-update'),

]