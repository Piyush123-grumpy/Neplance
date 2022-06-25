# Generated by Django 4.0 on 2022-06-24 16:14

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_freelancer', models.BooleanField(default=False)),
                ('is_employer', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=30, null=True, verbose_name='Language')),
                ('education', models.CharField(blank=True, max_length=30, null=True, verbose_name='Education')),
                ('current_job', models.CharField(blank=True, max_length=100, null=True, verbose_name='Current Job')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country')),
                ('profile_picture', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Porject Title')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Description')),
                ('date', models.DateField(blank=True, null=True)),
                ('freelancer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.freelancer')),
            ],
        ),
        migrations.CreateModel(
            name='Other_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SUbject', models.CharField(blank=True, max_length=100, null=True, verbose_name='Subject')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Description')),
                ('freelancer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.freelancer')),
            ],
        ),
        migrations.CreateModel(
            name='employment_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=100, null=True, verbose_name='Company')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('Title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('period', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Description')),
                ('freelancer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.freelancer')),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('PhoneNumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('profile_picture', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Description')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
    ]
