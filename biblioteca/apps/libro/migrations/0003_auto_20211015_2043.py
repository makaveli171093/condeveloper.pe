# Generated by Django 3.2.7 on 2021-10-16 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_alter_autor_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(max_length=150, verbose_name='Tu Nombre'),
        ),
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255, verbose_name='Titulo')),
                ('fecha_publicacion', models.DateField(verbose_name='fecha de publicacion')),
                ('autor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='libro.autor')),
            ],
            options={
                'verbose_name': 'libro',
                'verbose_name_plural': 'libros',
                'ordering': ['titulo'],
            },
        ),
    ]
