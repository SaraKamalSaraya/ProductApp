# Generated by Django 3.2.22 on 2023-10-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='categories/imgs/'),
        ),
    ]