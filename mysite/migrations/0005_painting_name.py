# Generated by Django 3.2 on 2021-07-05 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20210705_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='name',
            field=models.CharField(default='OP', max_length=20),
        ),
    ]
