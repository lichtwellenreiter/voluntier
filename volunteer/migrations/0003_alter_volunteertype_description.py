# Generated by Django 4.1.2 on 2022-10-20 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0002_volunteertypes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteertype',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
