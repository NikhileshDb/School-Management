# Generated by Django 3.2.5 on 2021-07-23 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210723_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]