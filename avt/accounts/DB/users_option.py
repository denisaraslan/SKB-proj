from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .managers import UserManager
from accounts.DB.lesson_option import Course, Module

class UserRole(models.TextChoices):
    STUDENT = "student"
    TEACHER = "teacher"
    ADMIN = "admin"

class ProgressStatus(models.TextChoices):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class User(models.Model):
    email = models.EmailField(unique=True, max_length=255)
    user_name = models.CharField(max_length=100)
    role = models.CharField(choices=UserRole.choices, default=UserRole.STUDENT)
    hashed_password = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    objects = UserManager()
    def __str__(self):
        return self.email


class UserCourseProgress(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "course"], name="uq_user_course")
        ]
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="course_progress")
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    percentage = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    update_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        choices=ProgressStatus.choices,
        default=ProgressStatus.NOT_STARTED,
    )

    def __str__(self):
        return self.status



class UserModuleProgress(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'module'],
                name='uq_user_module'
            )
        ]

    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="module_progress")
    module = models.ForeignKey('Module', on_delete=models.CASCADE)
    percentage = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    update_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        choices=ProgressStatus.choices,
        default=ProgressStatus.NOT_STARTED,
    )

    def __str__(self):
        return self.status
