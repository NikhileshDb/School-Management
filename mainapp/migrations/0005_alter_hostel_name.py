# Generated by Django 3.2.5 on 2021-09-27 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210928_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
