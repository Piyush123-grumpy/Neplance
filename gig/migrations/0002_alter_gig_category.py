# Generated by Django 4.0.4 on 2022-05-29 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gig', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gig.category', unique=True),
        ),
    ]
