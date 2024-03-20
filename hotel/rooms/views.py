from django.shortcuts import render
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Room
from reservations.models import Reservation
from .serializers import RoomSerializer
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from django.db.models import Q
from django.utils import timezone



class RoomListAPIView(GenericViewSet, ListModelMixin):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    

class AvailableRoomsAPIView(GenericViewSet, ListModelMixin):
    serializer_class = RoomSerializer

    def get_queryset(self):
        check_in_date = self.request.GET.get('check_in_date')
        check_out_date = self.request.GET.get('check_out_date')
        capacity = self.request.GET.get('capacity')
        
        if not check_in_date or not check_out_date:
            return Room.objects.none()
        
        try:
            check_in_date = timezone.datetime.strptime(check_in_date, '%Y-%m-%d').date()
            check_out_date = timezone.datetime.strptime(check_out_date, '%Y-%m-%d').date()
        except ValueError:
            return Room.objects.none()

        reservations = Reservation.objects.filter(
            Q(check_in__lt=check_out_date) & Q(check_out__gt=check_in_date)
        )
        reserved_room_ids = reservations.values_list('room_id', flat=True)

        available_rooms = Room.objects.exclude(id__in=reserved_room_ids)
        if capacity:
            available_rooms = available_rooms.filter(capacity=capacity)

        return available_rooms

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

