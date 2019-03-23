# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-03 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("challenges", "0014_changed_code_name_field")]

    operations = [
        migrations.CreateModel(
            name="DatasetSplit",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("codename", models.CharField(max_length=100)),
            ],
            options={"db_table": "dataset_split"},
        )
    ]
