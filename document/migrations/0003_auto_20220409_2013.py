# Generated by Django 3.1 on 2022-04-09 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_propertydoc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertydoc',
            old_name='client_id',
            new_name='property_id',
        ),
    ]
