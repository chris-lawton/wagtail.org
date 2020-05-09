# Generated by Django 2.2.12 on 2020-05-08 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize', '0006_delete_language_model'),
        ('core', '0039_homepage_brands'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='is_source_translation',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='locale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_localize.Locale'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
    ]