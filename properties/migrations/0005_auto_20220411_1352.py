# Generated by Django 3.1 on 2022-04-11 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20220409_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='property_linked_to',
        ),
        migrations.AlterField(
            model_name='client',
            name='bank_details',
            field=models.CharField(blank=True, default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='client',
            name='documents',
            field=models.CharField(blank=True, default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='history',
            field=models.CharField(blank=True, default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='client',
            name='mobile',
            field=models.IntegerField(blank=True, default='none'),
        ),
    ]