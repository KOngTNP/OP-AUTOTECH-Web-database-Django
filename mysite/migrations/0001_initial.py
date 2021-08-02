# Generated by Django 3.2 on 2021-08-02 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cutting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(null=True)),
                ('datePublish', models.DateTimeField(auto_now_add=True, null=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('drawingNo', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('drawingDesc', models.TextField()),
                ('Quantity', models.IntegerField()),
                ('datePublish', models.DateTimeField(auto_now_add=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('drawingNo', 'datePublish'),
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(null=True)),
                ('machineNum', models.IntegerField(null=True)),
                ('datePublish', models.DateTimeField(auto_now_add=True, null=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True, null=True)),
                ('drawing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machinedrawing', to='mysite.drawing')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Quantity', models.IntegerField()),
                ('datePublish', models.DateTimeField(auto_now_add=True, null=True)),
                ('dateEnd', models.DateTimeField(auto_now_add=True, null=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True, null=True)),
                ('drawing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paintingdrawing', to='mysite.drawing')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Revise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numTimes', models.IntegerField()),
                ('reviseDesc', models.TextField()),
                ('datePublish', models.DateTimeField(auto_now_add=True, null=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True, null=True)),
                ('drawing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revisedrawing', to='mysite.drawing')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QcPainting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('datePublish', models.DateTimeField(auto_now_add=True, null=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True, null=True)),
                ('painting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qcpaintingpainting', to='mysite.painting')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Qc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('datePublish', models.DateTimeField(auto_now_add=True, null=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True, null=True)),
                ('cutting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qccutting', to='mysite.cutting')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qcmachine', to='mysite.machine')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('datePublish', models.DateTimeField(auto_now_add=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True)),
                ('drawing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='makerdrawing', to='mysite.drawing')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('jobNo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('projectName', models.CharField(max_length=80)),
                ('projectDesc', models.TextField()),
                ('datePublish', models.DateTimeField(auto_now_add=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='drawing',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drawingjob', to='mysite.job'),
        ),
        migrations.AddField(
            model_name='drawing',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('datePublish', models.DateTimeField(auto_now_add=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True)),
                ('drawing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentdrawing', to='mysite.drawing')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cutting',
            name='drawing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuttingdrawing', to='mysite.drawing'),
        ),
        migrations.AddField(
            model_name='cutting',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Assemby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('datePublish', models.DateTimeField(auto_now_add=True, null=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True, null=True)),
                ('drawing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assembydrawing', to='mysite.drawing')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
