# Generated by Django 5.1 on 2024-08-20 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EthereumPrice',
            new_name='EthereumPriceFeed',
        ),
    ]
