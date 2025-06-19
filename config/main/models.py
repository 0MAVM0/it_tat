from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    img = models.ImageField(upload_to='courses/', null=True, blank=True)
    description = models.TextField()
    beginning = models.TimeField(null=False, blank=False)
    duration = models.IntegerField(null=True, blank=True, default=2)
    times_a_week = models.IntegerField(null=True, blank=True, default=3)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self) -> str:
        return self.name
