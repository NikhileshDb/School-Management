# Generated by Django 3.2.5 on 2021-09-25 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210925_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='last_name',
        ),
    ]