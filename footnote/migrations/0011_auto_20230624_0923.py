# Generated by Django 3.2.18 on 2023-06-24 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footnote', '0010_footnote_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footnote',
            name='footnote_number',
        ),
        migrations.RemoveField(
            model_name='footnote',
            name='footnote_total',
        ),
        migrations.DeleteModel(
            name='FootNoteLineItem',
        ),
    ]