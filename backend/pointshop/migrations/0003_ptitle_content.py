# Generated by Django 3.2.12 on 2022-08-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointshop', '0002_rename_title_ptitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='ptitle',
            name='content',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
