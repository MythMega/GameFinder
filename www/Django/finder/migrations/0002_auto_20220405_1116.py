# Generated by Django 3.2.12 on 2022-04-05 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='finder/static/finder/img/game/'),
        ),
        migrations.AlterField(
            model_name='licence',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='finder/static/finder/img/licence/'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='finder/static/finder/img/platform/'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='date_creation',
            field=models.DateField(default=datetime.date(2022, 4, 5)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='finder/static/finder/img/tag/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='account_creation',
            field=models.DateField(default=datetime.date(2022, 4, 5)),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture_profile',
            field=models.ImageField(blank=True, null=True, upload_to='finder/static/finder/img/user/banner_pic'),
        ),
    ]
