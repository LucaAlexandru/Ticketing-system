from django.db import models
from tickets.constants import STATUS_CHOICES
from django.contrib.auth.models import User

class TicketTemplate(models.Model):
    color = models.CharField(max_length=20)
    font = models.CharField(max_length=20)


class Ticket(models.Model):
    code = models.CharField(max_length=7)
    bug = models.CharField(max_length=50)
    created = models.DateField(null=True)
    assignee = models.CharField(max_length=50)
    due = models.DateField(null=True)
    status = models.CharField(max_length=20)
    severity = models.CharField(max_length=20, choices=STATUS_CHOICES, default="major")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(TicketTemplate, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.code


class Comments(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=500)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)