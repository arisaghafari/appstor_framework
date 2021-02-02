# Generated by Django 3.1.5 on 2021-02-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='images')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField()),
                ('rateCounter', models.IntegerField()),
                ('Rate', models.FloatField()),
                ('status', models.CharField(choices=[('p', 'pay'), ('n', 'without pay')], max_length=1)),
            ],
        ),
    ]