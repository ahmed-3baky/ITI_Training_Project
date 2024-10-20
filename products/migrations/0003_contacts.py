# Generated by Django 5.1 on 2024-08-30 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_projects_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('email', models.TextField()),
                ('phone', models.CharField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='products.projects')),
            ],
        ),
    ]
