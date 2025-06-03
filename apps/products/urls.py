from django.urls import path
from . import views

urlpatterns = [
    path('test_json_view/', views.test_json_view),
    path('test_post_view/', views.test_post_view),
    path('products/', views.ProductList.as_view()),
    path('products/expensive/', views.MostExpensiveProduct.as_view()),
    path('products/create/', views.ProductCreate.as_view()),
    path('products/<int:pk>/update/', views.ProductUpdate.as_view()),
]
