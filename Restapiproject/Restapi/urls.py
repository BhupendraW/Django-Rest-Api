from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('products/create/', views.product_create, name='product-create'),

    path('categories/', views.category_list, name='category-list'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),
    path('categories/create/', views.category_create, name='category-create'),

    path('tags/', views.tag_list, name='tag-list'),
    path('tags/<int:pk>/', views.tag_detail, name='tag-detail'),

    path('tags/create/', views.tag_create, name='tag-create'),
]
