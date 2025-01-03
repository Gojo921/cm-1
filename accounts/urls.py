from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home' ),
    path('products/', views.products, name='products' ),  
    path('customers/<str:pk>/', views.customers, name='customers' ),   
    path('create_order/<str:pk>/', views.createOrder, name='create_order' ),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order' ), 
    path('delete_order/<str:pk>/', views.DeleteOrder, name='delete_order' ),
    path('register/', views.register, name='register'), 
    path('login/', views.loginPage, name='login' ),
    path('logout/', views.logout__view, name='logout' ), 
    path('account/', views.accountsettings, name='account' ), 
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password" ), 
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"), 
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_view" ), 
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete" ), 
    
 

   
    
]
