# Generated by Django 3.2 on 2021-09-29 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_auto_20210925_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='machine',
            field=models.CharField(max_length=20, null=True),
        ),
    ]