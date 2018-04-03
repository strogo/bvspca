# Generated by Django 2.0.3 on 2018-04-03 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180326_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='banner_image',
            field=models.ForeignKey(blank=True, help_text='This image should be exactly 1400px wide and 370px high.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='page banner image'),
        ),
    ]
