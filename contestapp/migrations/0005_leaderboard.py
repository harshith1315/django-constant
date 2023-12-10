# Generated by Django 4.2.5 on 2023-12-10 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contestapp', '0004_alter_time_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
