# Generated by Django 3.1.6 on 2021-04-27 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_game_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='age_limit',
            field=models.SmallIntegerField(default=16),
        ),
    ]
