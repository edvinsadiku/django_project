# Generated by Django 4.2 on 2023-04-27 14:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webi', '0018_remove_shpallje_author_delete_projektet_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lajmet',
            new_name='Postimet',
        ),
    ]