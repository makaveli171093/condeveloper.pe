# Generated by Django 3.2.7 on 2021-10-16 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0004_alter_libro_autor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='fecha modificacion'),
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='fecha modificacion'),
        ),
    ]
