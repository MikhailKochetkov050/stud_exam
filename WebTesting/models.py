from django.db import models
from TestCreation.models import Questions, TeacherTests
from TestSystem.models import SignUp_Model

class StudTests(models.Model):
    # Модель с пройденными тестами
    user = models.ForeignKey(SignUp_Model, on_delete=models.CASCADE)
    best_result = models.IntegerField(default=0)
    attempts_count = models.IntegerField(default=0)
    test = models.ForeignKey(TeacherTests, on_delete=models.CASCADE)


class Attempts(models.Model):
    # Модель, хранящая результаты попыток прохождения тестов
    attempt_number = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    time = models.IntegerField(default=0)
    result = models.IntegerField(default=0)
    passed_test = models.ForeignKey(StudTests, on_delete=models.CASCADE)

class StudAnswers(models.Model):
    # Модель, хранящая ответы студентов
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choosen_answer1 = models.BooleanField(default=False)
    choosen_answer2 = models.BooleanField(default=False)
    choosen_answer3 = models.BooleanField(default=False)
    choosen_answer4 = models.BooleanField(default=False)
    iscorrect = models.BooleanField(default=False)
    attempt = models.ForeignKey(Attempts, on_delete=models.CASCADE)
