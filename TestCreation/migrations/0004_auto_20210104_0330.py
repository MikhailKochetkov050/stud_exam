# Generated by Django 3.1.4 on 2021-01-04 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestCreation', '0003_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]