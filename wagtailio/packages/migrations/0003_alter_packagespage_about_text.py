# Generated by Django 3.2.8 on 2022-01-28 09:49

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_add_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagespage',
            name='about_text',
            field=wagtail.core.fields.RichTextField(default='<p> Projects listed on Wagtail.org are <i>third-party</i> packages.<br/> They are not vetted nor endorsed by Wagtail.<br/> Use them at your own risk.</p> <p>This page collects girds and packages from djangopackages.org.<br/> Please add or update Wagtail grids and Wagtail packages on djangopackages.org. </p>'),
        ),
    ]
