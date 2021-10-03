# Generated by Django 3.2 on 2021-09-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_auto_20210915_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drawing',
            name='drawingDesc',
        ),
        migrations.RemoveField(
            model_name='job',
            name='projectDesc',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='machineNum',
        ),
        migrations.AddField(
            model_name='machine',
            name='machine',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]