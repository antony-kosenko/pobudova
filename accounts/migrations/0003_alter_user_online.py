# Generated by Django 4.1.7 on 2023-04-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_online'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
