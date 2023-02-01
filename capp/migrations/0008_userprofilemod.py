# Generated by Django 4.1.5 on 2023-01-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0007_alter_userprofilemodel_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofilemod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='capp/static')),
                ('fname', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('resume', models.FileField(upload_to='capp/static')),
                ('qualify', models.CharField(max_length=70)),
                ('exp', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=70)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
