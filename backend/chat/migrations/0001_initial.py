# Generated by Django 3.2.12 on 2022-08-11 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizRoom',
            fields=[
                ('roomnum', models.IntegerField(primary_key=True, serialize=False)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_room', to='quiz.quizlist')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_room', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuizUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='chat.quizroom')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_room', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuizAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_questions', to='quiz.quizquestions')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_answer', to='chat.quizroom')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_answer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
