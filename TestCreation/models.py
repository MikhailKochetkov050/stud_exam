from django.db import models
from TestSystem.models import SignUp_Model

class TeacherTests(models.Model):
    test_name = models.CharField("Название теста", max_length=500)
    question_count = models.IntegerField(default=0)
    attempt_count = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    user_id =  models.ForeignKey(SignUp_Model, on_delete=models.CASCADE)

class Questions(models.Model):
    question = models.TextField(max_length=1000)
    prompt = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    manychoises = models.BooleanField(default=False)
    test_id = models.ForeignKey(TeacherTests, on_delete=models.CASCADE)
    answer1 = models.CharField("Вариант 1", max_length=200)
    isright1 = models.BooleanField(default=False)
    answer2 = models.CharField("Вариант 2", max_length=200)
    isright2 = models.BooleanField(default=False)
    answer3 = models.CharField("Вариант 3", max_length=200)
    isright3 = models.BooleanField(default=False)
    answer4 = models.CharField("Вариант 4", max_length=200)
    isright4 = models.BooleanField(default=False)
