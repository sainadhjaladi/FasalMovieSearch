# Generated by Django 4.1.7 on 2024-05-31 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasalapp', '0002_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='movie_poster',
            field=models.CharField(max_length=255),
        ),
    ]