# Generated by Django 4.2 on 2023-04-17 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webi', '0004_alter_lajmet_options_shpallje_projektet'),
    ]

    operations = [
        migrations.AddField(
            model_name='lajmet',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='images/'),
        ),
    ]