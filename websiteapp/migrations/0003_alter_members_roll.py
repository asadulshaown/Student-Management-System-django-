# Generated by Django 5.2.1 on 2025-05-22 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0002_members_delete_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='roll',
            field=models.CharField(max_length=50),
        ),
    ]
