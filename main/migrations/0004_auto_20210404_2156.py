# Generated by Django 3.1.6 on 2021-04-04 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210404_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='category',
            field=models.ManyToManyField(blank=True, default=None, related_name='category', to='main.Category'),
        ),
    ]
