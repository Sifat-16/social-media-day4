# Generated by Django 3.0.9 on 2020-09-01 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='admin@mail.com', max_length=200),
        ),
    ]