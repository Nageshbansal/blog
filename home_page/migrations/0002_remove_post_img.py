# Generated by Django 3.2.2 on 2021-05-22 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
    ]
