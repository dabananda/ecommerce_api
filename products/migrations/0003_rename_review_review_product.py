# Generated by Django 5.2.3 on 2025-06-14 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='product',
        ),
    ]
