# Generated by Django 5.1 on 2024-09-23 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='username',
        ),
    ]