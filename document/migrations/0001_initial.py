# Generated by Django 3.1 on 2022-04-09 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '0004_auto_20220409_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_file', models.FileField(upload_to='static/documents/')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.client')),
            ],
        ),
    ]
