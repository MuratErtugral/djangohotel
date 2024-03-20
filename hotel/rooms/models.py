from django.db import models

class Room(models.Model):
    capacity = models.IntegerField()

    def __str__(self):
        return f"Room {self.id} - {self.capacity} people"