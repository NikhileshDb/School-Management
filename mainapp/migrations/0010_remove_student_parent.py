# Generated by Django 3.2.5 on 2022-01-21 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20220119_0137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='parent',
        ),
    ]