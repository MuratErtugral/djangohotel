from django.db import models

class Reservation(models.Model):
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    trin = models.CharField(max_length=11)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname}"