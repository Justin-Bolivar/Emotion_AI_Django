# Generated by Django 5.0.4 on 2024-04-09 12:46

import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_alter_journal_emotion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='emotion',
            field=jsonfield.fields.JSONField(),
        ),
    ]
