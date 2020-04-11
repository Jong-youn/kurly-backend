# Generated by Django 2.1 on 2020-04-11 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('landing_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('banner_image', models.URLField(null=True)),
                ('landing_url', models.URLField(null=True)),
            ],
            options={
                'db_table': 'notices',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('landing_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'recipes',
            },
        ),
    ]
