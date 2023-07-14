# Generated by Django 4.2.1 on 2023-07-11 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_sharredtask_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharredtask',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='app.task'),
            preserve_default=False,
        ),
    ]
