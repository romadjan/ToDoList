# Generated by Django 3.2.5 on 2021-07-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_description',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
