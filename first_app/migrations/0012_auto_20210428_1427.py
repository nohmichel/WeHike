# Generated by Django 3.1.7 on 2021-04-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0011_auto_20210428_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to='images/'),
        ),
    ]
