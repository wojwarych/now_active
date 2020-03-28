# Generated by Django 2.2.10 on 2020-03-28 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20200328_2112'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
                ('open_from', models.DateTimeField()),
                ('closed_at', models.DateTimeField()),
                ('trainer', models.ManyToManyField(related_name='trainings_trainers', to='users.Trainer')),
            ],
        ),
        migrations.CreateModel(
            name='PlayersClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced')], max_length=1)),
                ('training_date', models.DateTimeField()),
                ('players', models.ManyToManyField(related_name='class_students', to=settings.AUTH_USER_MODEL)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainer_classes', to='users.Trainer')),
                ('training_place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager.TrainingPlace')),
            ],
        ),
    ]
