# Generated by Django 3.1.7 on 2021-04-28 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0008_auto_20210425_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trailfam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('location', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('website', models.CharField(max_length=100)),
            ],
        ),
    ]
