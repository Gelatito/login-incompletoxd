# Generated by Django 3.2.9 on 2021-11-22 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='contrasena',
        ),
    ]
