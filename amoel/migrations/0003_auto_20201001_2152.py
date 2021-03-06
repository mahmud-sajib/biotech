# Generated by Django 2.2.15 on 2020-10-01 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amoel', '0002_auto_20201001_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otutable',
            old_name='table_hash',
            new_name='tab_hash',
        ),
        migrations.RenameField(
            model_name='reference_sequence',
            old_name='hash',
            new_name='ref_hash',
        ),
        migrations.RemoveField(
            model_name='taxonomic',
            name='hash',
        ),
        migrations.AddField(
            model_name='taxonomic',
            name='tax_hash',
            field=models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taxonomics', to='amoel.OtuTable'),
        ),
    ]
