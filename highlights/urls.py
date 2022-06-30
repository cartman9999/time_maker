from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    
    path('', views.home, name='home'),
    path('user/', views.userPage, name='user_page'),
    # path('products/', views.products, name='products'),
    path('highlight/<str:pk>', views.highlight, name='highlight'),
    
    path('create_highlight', views.createHighlight, name='create_highlight'),
    path('update_highlight/<str:pk>', views.updateHighlight, name='update_highlight'),
    path('delete_highlight/<str:pk>', views.deleteHighlight, name='delete_highlight'),
]
