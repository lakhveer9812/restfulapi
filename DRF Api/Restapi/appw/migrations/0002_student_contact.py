# Generated by Django 3.2.8 on 2021-10-19 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='contact',
            field=models.CharField(default='', max_length=12),
        ),
    ]
