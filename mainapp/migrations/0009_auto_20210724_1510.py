# Generated by Django 3.2.5 on 2021-07-24 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_merge_20210724_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.classroom'),
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.teacher'),
        ),
    ]
