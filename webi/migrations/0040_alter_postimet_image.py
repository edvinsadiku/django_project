# Generated by Django 4.2 on 2023-05-01 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webi', '0039_alter_postimet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimet',
            name='image',
            field=models.ImageField(blank=True, default='images/ambienti-cover.jpg', null=True, upload_to='images/'),
        ),
    ]
