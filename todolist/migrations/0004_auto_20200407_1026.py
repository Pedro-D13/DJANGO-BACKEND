# Generated by Django 3.0.5 on 2020-04-07 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_habit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='todolist_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='todolist.TodoList'),
        ),
    ]
