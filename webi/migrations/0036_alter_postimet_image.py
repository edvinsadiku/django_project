# Generated by Django 4.2 on 2023-05-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webi', '0035_alter_postimet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimet',
            name='image',
            field=models.ImageField(blank=True, default='webi\\static\\img\x07mbienti-cover.jpg', null=True, upload_to='images/'),
        ),
    ]