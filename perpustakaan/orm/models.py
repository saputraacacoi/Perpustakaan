from django.db import models
from django.contrib.auth.models import User
import time
import os

class Anggota(models.Model):
    nama = models.CharField(max_length=100)
    PRIA = 'PR'
    WANITA = 'WN'
    JK_CHOICES  = (
        (PRIA, 'Pria'),
        (WANITA, 'Wanita'),
    )
    jenis_kelamin = models.CharField(
        max_length=2,
        choices=JK_CHOICES,
        default=PRIA,
    )
    alamat = models.CharField(max_length=100)
    masa_berlaku = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'Anggota'
        ordering = ['id']
