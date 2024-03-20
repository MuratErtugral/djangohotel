from django.urls import path, include
from . import views

app_name = 'reservations'

urlpatterns = [
    path('list/', views.ReservationCreateAPIView.as_view(actions={'get': 'list'}), name='list'),
    path('create/', views.ReservationCreateAPIView.as_view(actions={'post': 'create'}), name='create'),

]