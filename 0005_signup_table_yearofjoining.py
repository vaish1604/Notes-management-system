# Generated by Django 3.2.2 on 2021-05-12 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_rename_signup_signup_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup_table',
            name='yearofjoining',
            field=models.CharField(default=2020, max_length=100),
        ),
    ]