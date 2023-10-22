from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_order/', views.create_order, name='create_order'),
    path('order/<int:id>/', views.order_edit, name='order'),
    path('order/<int:id>/product/', views.add_product, name='add_product'),
    path('order/<int:id>/delete_product/',
         views.delete_product, name='delete_product'),
]
