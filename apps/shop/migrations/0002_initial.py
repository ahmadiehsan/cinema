# Generated by Django 3.2.9 on 2022-03-03 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserves', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='release',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.movie', verbose_name='Movie'),
        ),
        migrations.AddField(
            model_name='release',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.room', verbose_name='Room'),
        ),
        migrations.AddField(
            model_name='movie',
            name='rooms',
            field=models.ManyToManyField(related_name='movies', through='shop.Release', to='shop.Room'),
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('room', 'row', 'number')},
        ),
        migrations.AlterUniqueTogether(
            name='reserve',
            unique_together={('seat', 'release', 'user')},
        ),
    ]
