# Generated by Django 4.2 on 2023-11-15 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_user_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]