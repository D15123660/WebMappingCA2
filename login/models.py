# login/models.py

from django.db import models


class User(models.Model):
    gender = (
        'male', 'Male',
        'female', 'Female',
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='Male')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = 'User'
        verbose_name_plural = 'User'

    class Location(models.Model):
        name = models.CharField(max_length=50, default='Unknown location')
        mpoint = models.PointField()

        def __str__(self):
            return self.name
