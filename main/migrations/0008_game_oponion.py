# Generated by Django 3.1.6 on 2021-04-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210406_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='oponion',
            field=models.IntegerField(blank=True, default=15),
        ),
    ]
