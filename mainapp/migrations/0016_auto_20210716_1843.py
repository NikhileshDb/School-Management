# Generated by Django 3.2.5 on 2021-07-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_profileimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, default='media/default.png', null=True, upload_to='profile_pic/', verbose_name='Image'),
        ),
    ]
