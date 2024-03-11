# Generated by Django 3.2.25 on 2024-03-11 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('poster', models.URLField()),
                ('genre', models.CharField(max_length=255)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('year_release', models.IntegerField()),
                ('metacritic_rating', models.IntegerField(blank=True, null=True)),
                ('runtime', models.IntegerField()),
            ],
        ),
    ]
