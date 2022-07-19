# Generated by Django 4.1b1 on 2022-07-19 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0006_alter_photo_room_alter_room_amenities_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("reservations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="guest",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservations",
                to="rooms.room",
            ),
        ),
    ]
