# Generated by Django 4.0.5 on 2022-07-12 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0003_profesor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='materia',
            new_name='profesion',
        ),
    ]
