# Generated by Django 5.0.4 on 2024-04-12 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('named_url', models.CharField(blank=True, max_length=100, null=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='myapp.menuitem')),
            ],
        ),
    ]
