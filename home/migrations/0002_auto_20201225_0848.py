# Generated by Django 3.1.4 on 2020-12-25 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'masin', 'verbose_name_plural': 'masinlar'},
        ),
        migrations.AlterModelTable(
            name='car',
            table='car',
        ),
    ]
