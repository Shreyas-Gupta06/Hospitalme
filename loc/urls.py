from django.urls import path
from . import views

app_name = 'loc'

urlpatterns = [
    path('map/', views.map, name='map'),
    path('hospital/<path:hospital_name>/', views.hospital_info, name='hospital_info'),
    path('hospital_list/', views.hospital_list, name='hospital_list'),

]
