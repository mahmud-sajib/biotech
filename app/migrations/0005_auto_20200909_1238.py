# Generated by Django 2.2.15 on 2020-09-09 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_otumetatable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otutable',
            name='sa_1',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='sa_10',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='sa_11',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='sa_12',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='sa_13',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='sa_14',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='sa_15',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='sa_2',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='sa_3',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='sa_4',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='sa_5',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='sa_6',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='sa_7',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='sa_8',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='sa_9',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='otutable',
            name='seq',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.CreateModel(
            name='TaxonomicTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kingdom', models.CharField(max_length=50)),
                ('phylum', models.CharField(max_length=50)),
                ('taconomy_class', models.CharField(max_length=50)),
                ('order', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=50)),
                ('genus', models.CharField(max_length=50)),
                ('species', models.CharField(max_length=50)),
                ('seq', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.OtuTable')),
            ],
        ),
    ]
