# Generated by Django 5.1.4 on 2024-12-12 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_age_alter_profile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Biography here!', verbose_name='Biography'),
        ),
    ]
