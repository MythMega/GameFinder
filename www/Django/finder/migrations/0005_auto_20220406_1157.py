# Generated by Django 3.2.12 on 2022-04-06 09:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0004_auto_20220405_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='licence',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='date_creation',
            field=models.DateField(default=datetime.date(2022, 4, 6)),
        ),
        migrations.AlterField(
            model_name='user',
            name='account_creation',
            field=models.DateField(default=datetime.date(2022, 4, 6)),
        ),
    ]
