# Generated by Django 3.2.5 on 2021-07-28 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20210728_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAppearedExam',
            fields=[
                ('student_appeared_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.classroom')),
                ('exam', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.exam')),
                ('student', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.student')),
                ('subject', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.subject')),
            ],
        ),
    ]