from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    
    path('signup/', views.signup_view, name='signup'),
    
    
    path('tv_list/', views.tv_list_view, name='tv_list'),
    path('order_list/', views.order_list_view, name='order_list'),
    
    path('edit_tv/<int:product_id>/', views.update_product, name='edit_tv'),
    path('delete_tv/<int:id>/', views.delete_tv_view, name='delete_tv'),
    
     path('create_order/', views.create_order, name='create_order'),
     path('edit_order/<int:order_id>/', views.update_order, name='edit_order'),
     path('delete_order/<int:id>/', views.delete_order_view, name='delete_order'),
]
