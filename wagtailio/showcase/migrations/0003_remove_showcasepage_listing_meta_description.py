# Generated by Django 4.2.8 on 2024-03-11 22:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("showcase", "0002_populate_sectors"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="showcasepage",
            name="listing_meta_description",
        ),
    ]
