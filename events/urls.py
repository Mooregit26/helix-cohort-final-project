from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/add/', views.event_create, name='event_create'),
    path('sessions/<int:session_id>/book/',
    views.create_booking,name='create_booking'),
    path(
    'booking/confirmation/<int:booking_id>/',
    views.booking_confirmation,
    name='booking_confirmation'
),
]
