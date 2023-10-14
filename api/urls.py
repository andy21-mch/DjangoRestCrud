from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverView, name='home'),
    path('create/', views.add_item, name='add-items'),
    path('get_all/', views.get_items, name='get-items'),
    path('update/<int:pk>', views.update_item, name='update-item'),
    path('delete/<int:pk>', views.delete_item, name='delete-item'),
    path('get_by_id/<int:pk>', views.get_by_id, name='get-item-detail'),
]