from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    img = models.ImageField(upload_to='courses/', null=True, blank=True)
    description = models.TextField()
    beginning = models.TimeField(null=False, blank=False)
    duration = models.CharField(max_length=15, null=False, blank=False)      # 2 soat davomiyligi
    times_a_week = models.CharField(max_length=15, null=False, blank=False)  # 3 marta bir haftada
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Mentor(models.Model):
    full_name = models.CharField(max_length=255, null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='mentors/', null=True, blank=True)
    job_experience = models.CharField(max_length=20, null=False, blank=False)
    graduated_students = models.CharField(max_length=20, null=True,  blank=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.full_name
