# Generated by Django 4.0.5 on 2022-06-09 05:28

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('first_name', models.CharField(blank=True, max_length=32)),
                ('last_name', models.CharField(blank=True, max_length=32, null=True)),
                ('username', models.CharField(blank=True, editable=False, max_length=128)),
                ('email', models.EmailField(blank=True, max_length=128, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
