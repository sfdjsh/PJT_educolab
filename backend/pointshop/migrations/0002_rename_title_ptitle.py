# Generated by Django 3.2.12 on 2022-08-09 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20220809_2338'),
        ('pointshop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Title',
            new_name='PTitle',
        ),
    ]