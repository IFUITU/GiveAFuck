# Generated by Django 3.1.6 on 2021-04-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210405_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='count_dwnd',
            field=models.IntegerField(blank=True, default=16),
        ),
        migrations.AlterField(
            model_name='game',
            name='likes',
            field=models.IntegerField(blank=True, default=14),
        ),
    ]
