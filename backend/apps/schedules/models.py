from django.db import models
from apps.users.models import User
from apps.clients.models import Client

class Schedule(models.Model):
    TYPE_CHOICES = (
        ('daily', 'Diário'),
        ('weekly', 'Semanal'),
        ('monthly', 'Mensal'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    days_of_week = models.JSONField(null=True, blank=True)  # ["monday", "wednesday"]
    available_times = models.JSONField()  # ["09:00", "14:00"]
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pendente'),
        ('done', 'Realizado'),
        ('canceled', 'Cancelado')
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)

    def __str__(self):
        return f"{self.client.name} - {self.date} {self.time} - {self.status}"
