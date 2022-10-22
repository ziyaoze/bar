from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Booking(models.Model):
    name=models.CharField(max_length=50)

    timestamp=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
    barber=models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Shop(models.Model):

    status=models.BooleanField(default=False)

    @property
    def open(self):
        if self.status is False:
            return 'closed'
        else:
            return 'opened'

    @property
    def border(self):
        if self.status is False:
            return 'rgb(220,220,220, 0.4)'
        else:
            return 'green'


