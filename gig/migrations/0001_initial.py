# Generated by Django 4.0 on 2022-06-22 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(default='gigs/default.png', upload_to='gigs/')),
                ('description', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('pay', models.IntegerField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gig.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.user')),
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
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255, null=True)),
                ('applied_date', models.DateField(auto_now=True)),
                ('gig', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gig.gig')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
    ]
