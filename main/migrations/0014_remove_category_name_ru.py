# Generated by Django 3.1.5 on 2021-05-02 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_game_age_limit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name_ru',
        ),
    ]
