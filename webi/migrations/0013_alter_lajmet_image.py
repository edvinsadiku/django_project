# Generated by Django 4.2 on 2023-04-18 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webi', '0012_alter_lajmet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lajmet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='lajmet_images/'),
        ),
    ]
