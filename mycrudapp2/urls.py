from django.urls import path
from .views import intern_list, create_intern, update_intern, delete_intern

urlpatterns = [
    path('', intern_list, name='intern_list'),
    path('create/', create_intern, name='create_intern'),
    path('update/<int:intern_id>/', update_intern, name='update_intern'),
    path('delete/<int:intern_id>/', delete_intern, name='delete_intern'),
]
