# Generated by Django 4.1b1 on 2022-07-20 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("conversations", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="conversation",
            old_name="pasticipants",
            new_name="participants",
        ),
    ]
