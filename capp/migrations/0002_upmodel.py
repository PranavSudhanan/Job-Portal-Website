# Generated by Django 4.1.5 on 2023-01-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='upmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('jtitle', models.CharField(max_length=25)),
                ('jtype', models.CharField(max_length=25)),
                ('wtype', models.CharField(max_length=25)),
                ('exp', models.CharField(max_length=25)),
                ('qualify', models.CharField(max_length=70)),
            ],
        ),
    ]
