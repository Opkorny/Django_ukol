from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.ProductList.as_view(), name='list'),
    path('detail/<int:pk>', views.ProductDetail.as_view(), name='detail'),
    path('product/create/', views.ProductCreate.as_view(), name='product-create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product-delete'),
]