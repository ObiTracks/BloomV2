# Generated by Django 4.0 on 2022-03-05 18:02

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(max_length=200)),
                ('address_line_2', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('timeslots', models.JSONField(blank=True, null=True)),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='AmenityProfileRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_type', models.CharField(choices=[('0', 'Owner'), ('1', 'Manager'), ('2', 'Supervisor'), ('3', 'Staff'), ('4', 'Authorized User'), ('5', 'Member')], default='5', max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('amenity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenity_of', to='mainApp.amenity', verbose_name='Amenity in the relationship')),
            ],
            options={
                'verbose_name': 'Amenity Profile Relationship',
                'verbose_name_plural': 'Amenity Profile Relationships',
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainApp.address')),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200)),
                ('startime', models.TimeField(default=datetime.time(0, 0))),
                ('endtime', models.TimeField(default=datetime.time(0, 0))),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_show', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True, max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('amenity_profile_relationship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.amenityprofilerelationship', verbose_name='AmenityRelationship for the Reservation')),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation_set', to='mainApp.place')),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True)),
                ('bio', models.TextField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='accountsApp.customuser')),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='PlaceProfileRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_type', models.CharField(choices=[('0', 'Owner'), ('1', 'Manager'), ('2', 'Supervisor'), ('3', 'Staff'), ('4', 'Authorized User'), ('5', 'Member')], default='Member', max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_of', to='mainApp.place', verbose_name='Place in the relationship')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_profile_of', to='mainApp.profile', verbose_name='Profile in the relationship')),
            ],
            options={
                'verbose_name': 'Place Profile Relationship',
                'verbose_name_plural': 'Place Profile Relationships',
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='JoinRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.place')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.profile')),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
        migrations.AddField(
            model_name='amenityprofilerelationship',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenity_profile_of', to='mainApp.profile', verbose_name='Profile in the relationship'),
        ),
        migrations.AddField(
            model_name='amenity',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.place'),
        ),
    ]