# Generated by Django 2.1.7 on 2019-04-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackauth', '0014_auto_20190403_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='slackaccount',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='date updated'),
        ),
        migrations.AddField(
            model_name='slackbottoken',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='date updated'),
        ),
        migrations.AddField(
            model_name='slackteam',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='date updated'),
        ),
        migrations.AddField(
            model_name='slackusertoken',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='slackaccount',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='slackbottoken',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_created'),
        ),
        migrations.AlterField(
            model_name='slackteam',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='slackusertoken',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_created'),
        ),
    ]
