# Generated by Django 4.0.6 on 2022-08-29 16:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0006_feed_bookmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='bookmark',
            field=models.ManyToManyField(related_name='bookmark', to=settings.AUTH_USER_MODEL, verbose_name='북마크'),
        ),
    ]
