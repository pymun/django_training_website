# Generated by Django 5.0.6 on 2024-05-24 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricetable',
            old_name='pc_new_price',
            new_name='pt_new_price',
        ),
        migrations.RenameField(
            model_name='pricetable',
            old_name='pc_old_price',
            new_name='pt_old_price',
        ),
        migrations.RenameField(
            model_name='pricetable',
            old_name='pc_title',
            new_name='pt_title',
        ),
    ]
