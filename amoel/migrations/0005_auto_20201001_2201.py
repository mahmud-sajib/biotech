# Generated by Django 2.2.15 on 2020-10-01 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amoel', '0004_auto_20201001_2200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otu_metad_id',
            old_name='hash',
            new_name='otu_hash',
        ),
    ]
