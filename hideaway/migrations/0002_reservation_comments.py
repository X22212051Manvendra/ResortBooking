# Generated by Django 3.0.7 on 2023-04-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hideaway', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='comments',
            field=models.CharField(default='Default comments', max_length=30),
        ),
    ]
