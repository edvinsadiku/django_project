# Generated by Django 4.2 on 2023-04-27 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webi', '0022_alter_lajmet_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lajmet',
            old_name='category',
            new_name='kategorite',
        ),
    ]
