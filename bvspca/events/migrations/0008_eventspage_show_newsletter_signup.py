# Generated by Django 2.0.4 on 2018-08-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20180411_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventspage',
            name='show_newsletter_signup',
            field=models.BooleanField(default=True),
        ),
    ]