# Generated by Django 4.1rc1 on 2022-07-31 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_email_secret_user_email_verified_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="login_method",
            field=models.CharField(
                choices=[("email", "Email"), ("kakao", "Kakao")],
                default="email",
                max_length=50,
            ),
        ),
    ]
