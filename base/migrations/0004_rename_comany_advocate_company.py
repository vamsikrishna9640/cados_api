# Generated by Django 4.0.6 on 2024-04-04 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_advocate_comany'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advocate',
            old_name='comany',
            new_name='company',
        ),
    ]
