from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='event_index'),
    path('upcoming-events/', views.upcoming_events, name='upcoming_events'),
    path('create-event/', views.create_event, name='create_event'),
]
