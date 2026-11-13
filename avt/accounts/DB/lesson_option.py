from django.db import models


class ModuleLevel(models.TextChoices):
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"

class StepType(models.TextChoices):
    MULTIPLE_CHOICE = "multiple_choice"
    FILL_IN_THE_BLANK = "fill_in_the_blank"

class ProgressStatus(models.TextChoices):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Module(models.Model):
    title = models.CharField(max_length=150)
    order = models.IntegerField()
    level = models.CharField(choices=ModuleLevel.choices)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=150)
    order = models.IntegerField()
    module = models.ForeignKey('Module', on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title

class Step(models.Model):
    order = models.IntegerField()
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=255, blank=True)
    type = models.CharField(choices=StepType.choices)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='step')

    # constraints = [
    #     models.UniqueConstraint(fields=["order", "lesson"], name="uq_lessons_step")
    # ]

    def __str__(self):
        return f'Step_{self.order}_Lesson_{self.lesson}'

class StepOption(models.Model):
    step = models.ForeignKey('Step', on_delete=models.CASCADE, related_name='option')
    option_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.step}'