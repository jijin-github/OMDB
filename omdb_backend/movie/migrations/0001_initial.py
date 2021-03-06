# Generated by Django 2.2.4 on 2019-08-06 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MovieDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rated', models.CharField(max_length=30)),
                ('imdbID', models.CharField(max_length=30, unique=True)),
                ('actors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Actor')),
            ],
        ),
    ]
