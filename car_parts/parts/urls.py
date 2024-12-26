from django.urls import path
from .views import car_list, part_list

urlpatterns = [
    path('', car_list, name='car_list'),
    path('parts/<int:car_id>/', part_list, name='part_list'),
]