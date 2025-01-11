# Generated by Django 5.1.4 on 2025-01-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venue",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="Email Address"
            ),
        ),
        migrations.AlterField(
            model_name="venue",
            name="web",
            field=models.URLField(blank=True, verbose_name="Website"),
        ),
    ]
