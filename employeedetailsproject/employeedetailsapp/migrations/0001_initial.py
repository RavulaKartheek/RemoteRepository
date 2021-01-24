# Generated by Django 3.1.2 on 2020-12-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.IntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('bonus', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('hire_date', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
