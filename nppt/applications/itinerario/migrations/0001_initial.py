# Generated by Django 2.0 on 2018-01-08 20:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('denomination', models.CharField(max_length=150, verbose_name='denominacion')),
                ('distance_foot', models.CharField(max_length=50, verbose_name='distancia pies')),
                ('altitude_place', models.CharField(max_length=70, verbose_name='altitud del lugar')),
                ('wheater', models.CharField(max_length=70, verbose_name='clima')),
                ('description', models.CharField(max_length=150, verbose_name='descripcion')),
            ],
            options={
                'verbose_name_plural': 'Itinerarios',
                'verbose_name': 'Itinerario',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('destiny', models.CharField(max_length=100, verbose_name='destino')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('title_seo', models.CharField(max_length=150, verbose_name='titulo seo')),
                ('description', models.CharField(max_length=150, verbose_name='descripcion')),
                ('description_seo', models.CharField(max_length=150, verbose_name='descripcion seo')),
                ('content', models.CharField(max_length=200, verbose_name='contenido')),
                ('tags', models.CharField(max_length=100, verbose_name='Tags')),
                ('visit', models.IntegerField(verbose_name='visitas')),
                ('slug', models.SlugField(editable=False, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Lugares',
                'verbose_name': 'Lugar',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='itinerary',
            name='place',
            field=models.ManyToManyField(to='itinerario.Place'),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.Service'),
        ),
    ]
