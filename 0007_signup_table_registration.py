# Generated by Django 3.2.2 on 2021-05-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0006_auto_20210512_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup_table',
            name='registration',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
    ]
