from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationCreateAPIView(CreateModelMixin, GenericViewSet, ListModelMixin):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        room_id = request.data.get('room')
        request_check_in = request.data.get('check_in')
        request_check_out = request.data.get('check_out')

        existing_reservation = Reservation.objects.filter(
            room_id=room_id,
            check_in__lt=request_check_out,
            check_out__gt=request_check_in
        ).exists()

        if existing_reservation:
            return Response({'error': 'Oda belirtilen tarihler arasında doludur.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
