from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllBooksView.as_view(), name='all_books'),
    path('login/', views.UsersLoginView.as_view(), name='login'),
    path('logout/', views.UsersLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterFormView.as_view(), name='register')
]
