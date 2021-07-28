# Generated by Django 3.2.5 on 2021-07-28 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_classroom_name_numeric'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('attendence_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.CharField(max_length=20)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('student_name', models.CharField(blank=True, max_length=30, null=True)),
                ('rollNo', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeacherAttendance',
            fields=[
                ('attendence_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.CharField(max_length=20)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('teacher_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='attendence',
        ),
        migrations.AlterField(
            model_name='classroom',
            name='name_numeric',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='teacherattendance',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.classroom'),
        ),
        migrations.AddField(
            model_name='teacherattendance',
            name='section_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.section'),
        ),
        migrations.AddField(
            model_name='teacherattendance',
            name='teacher_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.teacher'),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.classroom'),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='section_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.section'),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='student_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.student'),
        ),
    ]
