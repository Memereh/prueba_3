# Generated by Django 4.0.5 on 2022-07-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='USUARIO',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
    ]