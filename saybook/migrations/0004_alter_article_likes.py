# Generated by Django 3.2.13 on 2022-06-15 12:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saybook', '0003_article_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
