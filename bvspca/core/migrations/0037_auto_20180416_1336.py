# Generated by Django 2.0.4 on 2018-04-16 19:36

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20180413_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='slider',
            field=wagtail.core.fields.StreamField((('slider_item', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=25, required=False)), ('summary', wagtail.core.blocks.TextBlock(max_length=60, required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock(help_text='This image MUST BE EXACTLY 1400px by 475px')), ('page', wagtail.core.blocks.PageChooserBlock(required=False))))),), blank=True),
        ),
    ]
