# Generated by Django 4.0.5 on 2022-07-24 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig', '0002_gig_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gig',
            old_name='paid',
            new_name='employer_paid',
        ),
        migrations.AddField(
            model_name='gig',
            name='paid_freelancer',
            field=models.BooleanField(default=False),
        ),
    ]
