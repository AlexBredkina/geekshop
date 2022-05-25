# Generated by Django 2.2.17 on 2021-01-29 17:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210127_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='aktivation_key',
            new_name='activation_key',
        ),
        migrations.RemoveField(
            model_name='user',
            name='aktivation_key_expires',
        ),
        migrations.AddField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 31, 17, 39, 28, 333, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]