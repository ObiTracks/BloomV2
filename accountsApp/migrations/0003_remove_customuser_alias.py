# Generated by Django 4.0 on 2022-06-25 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountsApp', '0002_customuser_alias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='alias',
        ),
    ]
