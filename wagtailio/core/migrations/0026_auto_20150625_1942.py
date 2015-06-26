# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtaildocs.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailembeds.blocks
import wagtailio.utils.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_featurepage_page_ptr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('blockquote', wagtail.wagtailcore.blocks.CharBlock(icon='quote', classname='title')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('imagecaption', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock())), label='Image caption')), ('textimage', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('background', wagtailio.utils.blocks.BackgroundColourChoiceBlock()), ('alignment', wagtailio.utils.blocks.SimpleImageFormatChoiceBlock())), icon='image')), ('colourtext', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('background', wagtailio.utils.blocks.BackgroundColourChoiceBlock())), icon='pilcrow')), ('calltoaction', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('background', wagtailio.utils.blocks.BackgroundColourChoiceBlock())), icon='pilcrow')), ('tripleimage', wagtail.wagtailcore.blocks.StructBlock((('first_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('second_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('third_image', wagtail.wagtailimages.blocks.ImageChooserBlock())), icon='image')), ('stats', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('stat', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.CharBlock())), icon='code'))), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='code')))),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('blockquote', wagtail.wagtailcore.blocks.CharBlock(icon='quote', classname='title')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('imagecaption', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock())), label='Image caption')), ('textimage', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('background', wagtailio.utils.blocks.BackgroundColourChoiceBlock()), ('alignment', wagtailio.utils.blocks.SimpleImageFormatChoiceBlock())), icon='image')), ('colourtext', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('background', wagtailio.utils.blocks.BackgroundColourChoiceBlock())), icon='pilcrow')), ('calltoaction', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('background', wagtailio.utils.blocks.BackgroundColourChoiceBlock())), icon='pilcrow')), ('tripleimage', wagtail.wagtailcore.blocks.StructBlock((('first_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('second_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('third_image', wagtail.wagtailimages.blocks.ImageChooserBlock())), icon='image')), ('stats', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('stat', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.CharBlock())), icon='code'))), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='code')))),
            preserve_default=True,
        ),
    ]