from django.db import models


class Technologies(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    img = models.ImageField(upload_to='technologies/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    img = models.ImageField(upload_to='courses/', null=True, blank=True)
    description = models.TextField()
    has_ai = models.BooleanField(default=False)
    duration_of_course = models.CharField(max_length=15, null=False, blank=False)
    beginning = models.TimeField(null=False, blank=False)
    duration_of_a_lesson = models.CharField(max_length=15, null=False, blank=False)
    times_a_week = models.CharField(max_length=15, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    technology = models.ForeignKey(Technologies, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    img = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.title} - {self.mentor.full_name}'


class Mentor(models.Model):
    full_name = models.CharField(max_length=255, null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='mentors/', null=True, blank=True)
    job_experience = models.IntegerField(null=False, blank=False)
    graduated_students = models.IntegerField(null=True,  blank=True)
    description = models.TextField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.full_name


class Feedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=False, blank=False)
    video = models.FileField(upload_to='feedbacks/', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.full_name} - {self.course.name}'


class LessonsVideo(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    tutor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video = models.FileField(upload_to='lessons_videos/', null=False, blank=False)

    def __str__(self) -> str:
        return self.title


class Registration(models.Model):
    full_name = models.CharField(max_length=150, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.full_name


class ProgrammeRequest(models.Model):
    full_name = models.CharField(max_length=150, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) -> str:
        return self.full_name


class FAQ(models.Model):
    question = models.CharField(max_length=255, null=False, blank=False)
    responce = models.TextField(null=False, blank=False)

    def __str__(self) -> str:
        return self.question
