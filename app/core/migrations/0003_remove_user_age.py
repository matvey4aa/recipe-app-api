# Generated by Django 2.1.15 on 2020-01-01 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]
