# Generated by Django 4.0.5 on 2022-06-22 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, max_length=500)),
                ('rating', models.FloatField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.employer')),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.freelancer')),
            ],
        ),
    ]