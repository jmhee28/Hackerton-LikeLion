# Generated by Django 4.0.5 on 2022-08-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_auto_20220629_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_headhunter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_looking_job',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
    ]