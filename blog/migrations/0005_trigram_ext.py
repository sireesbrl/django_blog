# Generated by Django 5.1.4 on 2024-12-16 11:42

from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension

class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_post_tags"),
    ]

    operations = [
        TrigramExtension(),
    ]