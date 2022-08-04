# Generated by Django 4.0.6 on 2022-08-03 18:26

from django.db import migrations, models


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
                ('full_name', models.CharField(max_length=20, verbose_name='Full name')),
                ('unique_id', models.UUIDField(db_index=True, default=152263, editable=False, unique=True, verbose_name='Unique ID')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('is_email_verified', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phone_number', models.PositiveIntegerField(null=True)),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('joined_date', models.DateTimeField(auto_now_add=True, verbose_name='Joined date')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Last Login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
