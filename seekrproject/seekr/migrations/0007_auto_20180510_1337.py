# Generated by Django 2.0.5 on 2018-05-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekr', '0006_auto_20180510_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='todo_list',
            field=models.ManyToManyField(blank=True, null=True, to='seekr.TodoItem'),
        ),
    ]
