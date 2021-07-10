# Generated by Django 3.2 on 2021-07-10 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0002_alter_machine_machinenum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='painting',
            old_name='dateStart',
            new_name='datePublish',
        ),
        migrations.RemoveField(
            model_name='qcpainting',
            name='painting',
        ),
        migrations.AddField(
            model_name='painting',
            name='dateUpdate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='painting',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='qcpainting',
            name='drawing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qcpaintingdrawing', to='mysite.drawing'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='machineNum',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='maker',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='painting',
            name='dateEnd',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='painting',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]