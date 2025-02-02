from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.portfolio_home, name='portfolio_home'),
    path('portfolio/', views.portfolio_list, name='portfolio_list'),
    path('portfolio/<int:project_id>/', views.project_detail, name='project_detail'),
    path('portfolio/create/', views.portfolio_create, name='portfolio_create'),
    path('portfolio/<int:project_id>/update/', views.portfolio_update, name='portfolio_update'),
    path('portfolio/<int:project_id>/delete/', views.portfolio_delete, name='portfolio_delete'),
    path('logout/', views.custom_logout, name='logout'),
]
