# Generated by Django 5.2.1 on 2025-05-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0003_alter_members_roll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='id',
        ),
        migrations.AlterField(
            model_name='members',
            name='roll',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
