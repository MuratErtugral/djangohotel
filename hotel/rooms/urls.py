from django.urls import path, include
from . import views

app_name = 'rooms'

urlpatterns = [
    path('list/', views.RoomListAPIView.as_view(actions={'get': 'list'}), name='list'),
    path('availablerooms/', views.AvailableRoomsAPIView.as_view(actions={'get': 'list'}), name='availablerooms'),

]