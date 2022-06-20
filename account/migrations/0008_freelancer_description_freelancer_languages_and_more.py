# Generated by Django 4.0.1 on 2022-05-19 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_freelancer'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='Description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='Languages',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='Skills',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='education',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
