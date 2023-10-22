from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_order/', views.create_order, name='create_order'),
    path('order/<int:id>/', views.order_edit, name='order'),
]
