# Generated by Django 4.2 on 2023-11-14 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrercomment',
            old_name='carrers',
            new_name='carrers_id',
        ),
    ]