# Generated by Django 3.1.6 on 2021-04-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210411_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='oponion',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='rated_user',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]