# Generated by Django 3.1.7 on 2021-04-21 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=80)),
                ('fav_hike', models.CharField(max_length=80)),
                ('bucket_list', models.CharField(max_length=80)),
                ('snack', models.CharField(max_length=80)),
                ('hike_need', models.CharField(max_length=80)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bio_uploaded', to='first_app.user')),
            ],
        ),
    ]
