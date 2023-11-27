from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_order/', views.create_order, name='create_order'),
    path('checkout/<order_id>', views.checkout, name='checkout'),
    path('order/<id>/', views.order_edit, name='order'),
    path('order/<id>/delete_order', views.delete_order, name='delete_order'),
    path('order/<id>/product/', views.add_product, name='add_product'),
    path('order/<id>/delete_product/',
         views.delete_product, name='delete_product'),
]
