# Generated by Django 3.2 on 2021-07-07 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_maker_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maker',
            name='drawing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='makerdrawing', to='mysite.drawing'),
        ),
    ]
