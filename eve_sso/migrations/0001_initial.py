# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-24 18:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('access_token', models.CharField(help_text='The access token granted by SSO.', max_length=254, unique=True)),
                ('refresh_token', models.CharField(blank=True, help_text='A re-usable token to generate new access tokens upon expiry. Only applies when scopes are granted by SSO.', max_length=254, null=True)),
                ('character_id', models.IntegerField(help_text='The ID of the EVE character who authenticated by SSO.')),
                ('character_name', models.CharField(help_text='The name of the EVE character who authenticated by SSO.', max_length=100)),
                ('token_type', models.CharField(choices=[('Character', 'Character'), ('Corporation', 'Corporation')], default='Character', help_text='The applicable range of the token.', max_length=100)),
                ('character_owner_hash', models.CharField(help_text='The unique string identifying this character and its owning EVE account. Changes if the owning account changes.', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CallbackCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Code used to retrieve access token from SSO.', max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CallbackRedirect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salt', models.CharField(help_text='Cryptographic salt used to generate the hash string.', max_length=32)),
                ('hash_string', models.CharField(help_text='Cryptographic hash used to reference this callback.', max_length=128)),
                ('url', models.CharField(default='/', help_text='The internal URL to redirect this callback towards.', max_length=254)),
                ('session_key', models.CharField(help_text='Session key identifying session this redirect was created for.', max_length=254, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('token', models.ForeignKey(blank=True, help_text='AccessToken generated by a completed code exchange from callback processing.', null=True, on_delete=django.db.models.deletion.CASCADE, to='eve_sso.AccessToken')),
            ],
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The official EVE name fot the scope.', max_length=100, unique=True)),
                ('help_text', models.TextField(help_text='The official EVE description of the scope.')),
            ],
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='scopes',
            field=models.ManyToManyField(blank=True, help_text='The access scopes granted by this SSO token.', to='eve_sso.Scope'),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='user',
            field=models.ForeignKey(blank=True, help_text='The user to whom this token belongs.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
