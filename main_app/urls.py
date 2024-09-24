from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('items/', views.shopping_list, name='shopping-list'),
    path('items/<int:item_id>/', views.item_detail, name='item-detail'),
    path('items/create', views.ItemCreate.as_view(), name='item-create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='item-update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),
]