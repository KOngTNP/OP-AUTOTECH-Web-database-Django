# Generated by Django 3.2 on 2021-10-04 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_remove_machine_machine'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='skipAssembly',
            field=models.BooleanField(default=True),
        ),
    ]
