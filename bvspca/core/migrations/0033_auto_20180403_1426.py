# Generated by Django 2.0.3 on 2018-04-03 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20180403_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoptioncentre',
            name='body',
        ),
        migrations.AlterField(
            model_name='adoptioncentre',
            name='cats_image',
            field=models.ForeignKey(blank=True, help_text='This image should be exactly 1400px wide and 370px high.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='cats banner image'),
        ),
    ]
