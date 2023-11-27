from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_order/', views.create_order, name='create_order'),
    path('checkout/<int:order_id>', views.checkout, name='checkout'),
    path('order/<int:id>/', views.order_edit, name='order'),
    path('order/<int:id>/delete_order', views.delete_order, name='delete_order'),
    path('order/<int:id>/product/', views.add_product, name='add_product'),
    path('order/<int:id>/delete_product/',
         views.delete_product, name='delete_product'),
]
