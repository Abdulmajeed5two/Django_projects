from django.urls import path,include
from shop import views
from . import views

urlpatterns = [
    path('home/', views.home_view, name="home"),
    path('header/', views.header_view, name='header'),
    path('footer/', views.footer_view, name='footer'),
    path('sections/', views.section_why, name='why'),
    path('sections', views.services, name='services'),
    path('sections', views.product_view, name='product_view'),
    path('about/', views.about_view, name="about"),
    path('contact/', views.contact_view, name="contact"),
    path('services/', views.services_view, name="services"),
    path('services/', views.services_list, name="services_list"),
    
    path('', include('users.urls')),
    
    path('', views.product_list, name='product_list'),
    # path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/add_review/', views.add_review, name='add_review'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_success/', views.order_success, name='order_success'),
    path('products/', views.all_products, name='all_products'),

]
