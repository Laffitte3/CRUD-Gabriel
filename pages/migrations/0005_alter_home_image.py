# Generated by Django 5.0.4 on 2024-06-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_home_alter_post_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="home",
            name="image",
            field=models.ImageField(upload_to="photos/background"),
        ),
    ]
