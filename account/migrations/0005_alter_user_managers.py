# Generated by Django 4.0.1 on 2022-05-15 09:38

import account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_is_employer_alter_user_is_freelancer'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
    ]
