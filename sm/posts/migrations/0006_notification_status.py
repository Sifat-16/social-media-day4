# Generated by Django 3.0.9 on 2020-09-04 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='status',
            field=models.CharField(choices=[('liked', 'liked'), ('commented', 'commented')], default='liked', max_length=9),
        ),
    ]
