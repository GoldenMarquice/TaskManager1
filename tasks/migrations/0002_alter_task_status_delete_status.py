# Generated by Django 4.2.4 on 2023-08-29 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'To Do'), (1, 'In Progress'), (2, 'Completed')], default=0),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
