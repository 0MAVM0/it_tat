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
    job_experience = models.IntegerField(null=False, blank=False)
    graduated_students = models.IntegerField(null=True,  blank=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.full_name


class Feedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=False, blank=False)
    video = models.FileField(upload_to='feedbacks/', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.full_name} - {self.course.name}"


class Portfolio(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    img = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title} - {self.mentor.full_name}"
