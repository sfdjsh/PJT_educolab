# Generated by Django 3.2.12 on 2022-08-10 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0012_alter_submithomework_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='submithomework',
            name='check_flag',
            field=models.BooleanField(default=False),
        ),
    ]
