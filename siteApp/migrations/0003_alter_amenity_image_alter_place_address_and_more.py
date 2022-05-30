# Generated by Django 4.0 on 2022-05-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0002_amenity_image_place_image_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
