# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('published', models.DateTimeField(null=True, blank=True)),
                ('bio', models.TextField(blank=True)),
                ('github_url', models.URLField()),
            ],
        ),
    ]
