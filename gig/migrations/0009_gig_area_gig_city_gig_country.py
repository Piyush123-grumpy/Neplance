# Generated by Django 4.0.5 on 2022-06-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig', '0008_alter_application_applied_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='area',
            field=models.CharField(default='Budhanilkantha', max_length=50),
        ),
        migrations.AddField(
            model_name='gig',
            name='city',
            field=models.CharField(default='Kathmandu', max_length=50),
        ),
        migrations.AddField(
            model_name='gig',
            name='country',
            field=models.CharField(default='Nepal', max_length=50),
        ),
    ]