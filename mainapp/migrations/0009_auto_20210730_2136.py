# Generated by Django 3.2.5 on 2021-07-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20210730_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]