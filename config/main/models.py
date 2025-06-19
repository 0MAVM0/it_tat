from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    img = models.ImageField(upload_to='courses/', null=True, blank=True)
    description = models.TextField()
    beginning = models.TimeField(null=False, blank=False)
    duration = models.IntegerField(null=False, blank=False, default=2)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    # tutor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
