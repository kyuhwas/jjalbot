# Generated by Django 2.1.7 on 2019-04-03 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slackauth', '0007_auto_20190403_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slacktoken',
            old_name='scopes',
            new_name='scope',
        ),
    ]
