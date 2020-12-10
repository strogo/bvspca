# Generated by Django 2.1.15 on 2020-12-10 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtaildocs', '0008_document_file_size'),
        ('core', '0042_auto_20181029_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedirectPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('link_external', models.URLField(blank=True, verbose_name='External link')),
                ('new_tab', models.BooleanField(blank=True, default=False, verbose_name='Open in new tab')),
                ('link_document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Redirect Page',
            },
            bases=('wagtailcore.page',),
        ),
    ]
