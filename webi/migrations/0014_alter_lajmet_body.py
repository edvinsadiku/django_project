# Generated by Django 4.2 on 2023-04-18 01:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webi', '0013_alter_lajmet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lajmet',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]