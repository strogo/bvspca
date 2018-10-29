# Generated by Django 2.0.4 on 2018-10-29 18:33

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20181029_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='slider',
            field=wagtail.core.fields.StreamField((('slider_item', wagtail.core.blocks.StructBlock((('photo', wagtail.images.blocks.ImageChooserBlock(help_text='This image MUST BE EXACTLY 1400px by 550px')), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(required=False)), ('active', wagtail.core.blocks.BooleanBlock(required=False))))),), blank=True),
        ),
    ]
