# Generated by Django 4.0.5 on 2022-07-06 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateField(auto_now=True)),
                ('status', models.CharField(default='Pending', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('company', models.CharField(max_length=50)),
                ('image', models.ImageField(default='gigs/default.png', upload_to='gigs/')),
                ('description', models.CharField(max_length=255, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('pay', models.IntegerField(null=True)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gig.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement', models.CharField(max_length=255)),
                ('gig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gig.gig')),
            ],
        ),
        migrations.CreateModel(
            name='Hired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freelancer_completed', models.BooleanField(default=False)),
                ('employer_verified', models.BooleanField(default=False)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gig.application')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='gig',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gig.gig'),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
