# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-04 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=20, unique=True)),
                ('cAge', models.IntegerField(default=0)),
                ('cEmail', models.CharField(default=None, max_length=20, null=True)),
                ('cDeclaration', models.CharField(default='我就是我，不一样的烟火', max_length=300)),
                ('cIcon', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('cTimes', models.IntegerField(default=1)),
                ('cVotes', models.IntegerField(default=0)),
                ('cPinyin', models.CharField(default='', max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'candidates',
                'ordering': ['-cVotes'],
            },
            managers=[
                ('cManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uName', models.CharField(max_length=20, unique=True)),
                ('uPwd', models.CharField(default=None, max_length=32, null=True)),
                ('uIP', models.CharField(max_length=20)),
                ('uEmail', models.CharField(default=None, max_length=20, null=True)),
                ('uNickName', models.CharField(default='guest', max_length=20, null=True)),
                ('uGender', models.NullBooleanField(default=None)),
                ('uAge', models.IntegerField(default=0)),
                ('uIcon', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('uToken', models.CharField(blank=True, default=None, max_length=64, null=True, unique=True)),
                ('uDateTime', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('uManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='VoteRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vDate', models.DateField(auto_now=True)),
                ('vTimes', models.IntegerField(default=1)),
                ('isDelete', models.BooleanField(default=False)),
                ('vCandidateId', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SitesApp.Candidate')),
            ],
            options={
                'db_table': 'voteRecords',
            },
            managers=[
                ('vManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='VoteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vType', models.CharField(max_length=20, unique=True)),
                ('vInfo', models.CharField(max_length=200)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'voteType',
            },
            managers=[
                ('vManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='voterecord',
            name='vTypeId',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SitesApp.VoteType'),
        ),
        migrations.AddField(
            model_name='voterecord',
            name='vUserId',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SitesApp.User'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='cVoteType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SitesApp.VoteType'),
        ),
    ]
