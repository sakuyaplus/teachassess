# Generated by Django 3.2.5 on 2021-07-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20210723_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='contact',
            field=models.TextField(blank=True),
        ),
    ]
