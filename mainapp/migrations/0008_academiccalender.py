# Generated by Django 3.2.5 on 2022-01-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_documents_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicCalender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
