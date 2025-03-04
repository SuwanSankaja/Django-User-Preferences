# Generated by Django 5.1.5 on 2025-02-02 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='data_sharing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='email_frequency',
            field=models.CharField(blank=True, choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='notification_preference',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_visibility',
            field=models.CharField(choices=[('private', 'Private'), ('public', 'Public')], default='private', max_length=10),
        ),
    ]
