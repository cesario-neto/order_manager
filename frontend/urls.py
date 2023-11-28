from django.urls import path
from . import views

urlpatterns = [
    # DashBoard
    path('', views.index, name='index'),
    path('/search/', views.search, name='search'),

    # Order
    path('create_order/', views.create_order, name='create_order'),
    path('checkout/<order_id>', views.checkout, name='checkout'),
    path('order/<id>/', views.order_edit, name='order'),
    path('order/<id>/delete_order', views.delete_order, name='delete_order'),

    # Product Order
    path('order/<id>/product/', views.add_product, name='add_product'),
    path('order/<order_id>/decrease/<product_id>/',
         views.decrease_quantity, name='decrease_quantity'),
    path('order/<order_id>/increase/<product_id>/',
         views.increase_quantity, name='increase_quantity'),

]
