# Generated by Django 4.0.5 on 2022-08-08 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0017_alter_user_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
    ]