# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('running','Running'),
    ('stopped','Stopped'),
    ('scheduled','Scheduled'),
)

class Userdetail(models.Model):
    driver_name      = models.CharField(max_length=120)
    phone            = models.CharField(max_length=120)
    vehicle_number   = models.CharField(max_length=120)
    latitude         = models.DecimalField(decimal_places=4,max_digits=20,null=True)
    longitude        = models.DecimalField(decimal_places=4,max_digits=20,null=True)
    status           = models.CharField(max_length=120, choices=STATUS_CHOICES, null=True)
    last_stoppage    = models.CharField(max_length=120)

    def __str__(self):
        return str(self.vehicle_number)

