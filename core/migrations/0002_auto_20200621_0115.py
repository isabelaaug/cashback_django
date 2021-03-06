# Generated by Django 3.0.7 on 2020-06-21 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100, unique=True)),
                ('cpf_compra', models.CharField(max_length=11)),
                ('data', models.DateTimeField(verbose_name='Data do Evento')),
                ('valor', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('percent_cashback', models.CharField(max_length=50)),
                ('cashback', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'compras',
            },
        ),
        migrations.AddField(
            model_name='usuario',
            name='public_id',
            field=models.CharField(default=125, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='token',
            field=models.CharField(default=456, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
