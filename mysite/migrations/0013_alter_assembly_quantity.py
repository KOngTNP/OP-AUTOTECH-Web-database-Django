# Generated by Django 3.2 on 2021-10-04 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_document_skipassembly'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assembly',
            name='Quantity',
            field=models.IntegerField(null=True),
        ),
    ]
