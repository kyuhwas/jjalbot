# Generated by Django 2.1.7 on 2019-03-29 14:08

import allauth.socialaccount.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlackAccount',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='socialaccount.SocialAccount')),
                ('slack_user_id', models.CharField(max_length=10)),
                ('extra_data', allauth.socialaccount.fields.JSONField(default=dict)),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='SlackTeam',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=21, unique=True)),
                ('verified', models.BooleanField(default=False)),
                ('extra_data', allauth.socialaccount.fields.JSONField(default=dict)),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='SlackToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField(verbose_name='token')),
                ('token_secret', models.TextField(blank=True, verbose_name='token secret')),
                ('expires_at', models.DateTimeField(blank=True, null=True, verbose_name='expires at')),
                ('scopes', models.TextField(verbose_name='scopes')),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='date created')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialaccount.SocialAccount')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialaccount.SocialApp')),
            ],
            options={
                'verbose_name': 'slack application token',
                'verbose_name_plural': 'slack application tokens',
            },
        ),
        migrations.AddField(
            model_name='slackaccount',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slackauth.SlackTeam'),
        ),
        migrations.AlterUniqueTogether(
            name='slacktoken',
            unique_together={('app', 'account', 'scopes')},
        ),
        migrations.AlterUniqueTogether(
            name='slackaccount',
            unique_together={('team', 'slack_user_id')},
        ),
    ]
