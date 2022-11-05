from django.db import models

class SignUp_Model(models.Model):
    USER_TYPES = (
        ('stud','Студент'),
        ('teacher','Преподаватель'),
        ('admin', 'Администратор'),
    )

    full_name= models.CharField("ФИО", max_length=100)
    user_type = models.CharField("Тип учетной записи", max_length=7, choices=USER_TYPES)
    username = models.CharField("Логин", max_length=100)
    # password = models.CharField('Пароль', max_length=100)
    login_attempts = models.IntegerField(default=0)
    locked = models.BooleanField(default=False)