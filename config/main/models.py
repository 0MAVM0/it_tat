from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='technologies/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='courses/', null=True, blank=True)
    description = models.TextField()
    has_ai = models.BooleanField(default=False)
    duration_of_course = models.CharField(max_length=15)
    beginning = models.TimeField()
    duration_of_a_lesson = models.CharField(max_length=15)
    times_a_week = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class Mentor(models.Model):
    full_name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='mentors/', null=True, blank=True)
    job_experience = models.IntegerField()
    graduated_students = models.IntegerField(null=True,  blank=True)
    description = models.TextField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.full_name


class Feedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    video = models.FileField(upload_to='feedbacks/', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.full_name} - {self.course.name}'


class LessonsVideo(models.Model):
    title = models.CharField(max_length=255)
    tutor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video = models.FileField(upload_to='lessons_videos/')

    def __str__(self) -> str:
        return self.title


class ProgramRequest(models.Model):
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.full_name


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    response = models.TextField()

    def __str__(self) -> str:
        return self.question


class WorldStatistics(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='world_statistics')
    junior_salary = models.DecimalField(max_digits=10, decimal_places=2)
    middle_salary = models.DecimalField(max_digits=10, decimal_places=2)
    senior_salary = models.DecimalField(max_digits=10, decimal_places=2)


class UzbStatistics(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='uzb_statistics')
    junior_salary = models.DecimalField(max_digits=10, decimal_places=2)
    middle_salary = models.DecimalField(max_digits=10, decimal_places=2)
    senior_salary = models.DecimalField(max_digits=10, decimal_places=2)
