# Generated by Django 4.0.4 on 2022-05-11 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0014_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Username')),
                ('email', models.EmailField(blank=True, max_length=100, unique=True, verbose_name='Email')),
                ('full_name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Phone Number')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('student_id', models.CharField(max_length=100, unique=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designate if the user has staff status', verbose_name='Staff Status')),
                ('is_active', models.BooleanField(default=True, help_text='Designate if the user has active status', verbose_name='Active Status')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designate if the user has superuser status', verbose_name='Superuser Status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
