# Generated by Django 4.1.2 on 2022-10-15 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
