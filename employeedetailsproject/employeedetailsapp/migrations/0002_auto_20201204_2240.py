# Generated by Django 3.1.2 on 2020-12-04 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeedetailsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeedetails',
            old_name='identity',
            new_name='emp_identity',
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='hire_date',
            field=models.CharField(max_length=100),
        ),
    ]
