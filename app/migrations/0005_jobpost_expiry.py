# Generated by Django 4.2.3 on 2023-09-07 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_jobpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='expiry',
            field=models.DateField(null=True),
        ),
    ]