# Generated by Django 3.2.12 on 2022-08-03 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20220803_0138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveyquestionsanswer',
            old_name='survey_question_pk',
            new_name='question',
        ),
    ]
