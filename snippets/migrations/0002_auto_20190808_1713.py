# Generated by Django 2.1.3 on 2019-08-08 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='highlited',
            new_name='highlighted',
        ),
    ]