# Generated by Django 3.2 on 2022-12-21 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('language', models.CharField(max_length=25)),
                ('date_started', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('month_to_learn', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('work_study_place', models.CharField(max_length=35, null=True)),
                ('has_own_notebook', models.BooleanField()),
                ('preferred_os', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('main_work', models.CharField(max_length=35, null=True)),
                ('experience', models.DateField()),
                ('student', models.ManyToManyField(related_name='mentors', through='user.Course', to='user.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.mentor'),
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student'),
        ),
    ]
