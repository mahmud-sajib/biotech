# Generated by Django 2.2.15 on 2020-09-12 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200909_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taxonomictable',
            old_name='taconomy_class',
            new_name='taxonomy_class',
        ),
    ]