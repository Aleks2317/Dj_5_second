# Generated by Django 5.1 on 2024-08-18 15:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.SmallIntegerField(null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('work_experience', models.SmallIntegerField(default=0)),
            ],
        ),
    ]
