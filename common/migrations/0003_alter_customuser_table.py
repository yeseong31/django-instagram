# Generated by Django 4.0.6 on 2022-07-15 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_customuser_thumbnail'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customuser',
            table='user',
        ),
    ]