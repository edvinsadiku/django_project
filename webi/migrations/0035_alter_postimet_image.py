# Generated by Django 4.2 on 2023-05-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webi', '0034_alter_document_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimet',
            name='image',
            field=models.ImageField(blank=True, default='ambienti-cover.jpg', null=True, upload_to='images/'),
        ),
    ]
