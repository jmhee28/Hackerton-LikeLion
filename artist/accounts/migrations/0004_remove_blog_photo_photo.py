# Generated by Django 4.0.5 on 2022-08-13 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_referring_user_blog_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='photo',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_photo')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.blog')),
            ],
        ),
    ]
