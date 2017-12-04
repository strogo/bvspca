# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 18:57
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0012_animal_updates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='updates',
            field=wagtail.wagtailcore.fields.StreamField((('heading_block', wagtail.wagtailcore.blocks.StructBlock((('heading_text', wagtail.wagtailcore.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))))), ('paragraph_block', wagtail.wagtailcore.blocks.RichTextBlock(icon='fa-paragraph', label='Paragraph')), ('image_block', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('block_quote', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock()), ('attribute_name', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))))), ('embed_block', wagtail.wagtailembeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-external-link-square', label='Embedded Media', template='core/blocks/embed_block.html')), ('table_block', wagtail.wagtailcore.blocks.StructBlock((('table', wagtail.contrib.table_block.blocks.TableBlock()), ('caption', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('raw_html', wagtail.wagtailcore.blocks.StructBlock((('html', wagtail.wagtailcore.blocks.RawHTMLBlock()),)))), blank=True, verbose_name='Animal Updates'),
        ),
    ]
