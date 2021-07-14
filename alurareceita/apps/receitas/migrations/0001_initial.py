# Generated by Django 3.2.5 on 2021-07-09 15:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.CharField(max_length=200)),
                ('ingredientes', models.TextField()),
                ('modo_preparo', models.TextField()),
                ('tempo_preparo', models.IntegerField()),
                ('rendimento', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('data_receita', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('foto_receita', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/')),
                ('publicada', models.BooleanField(default=False)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa')),
            ],
        ),
    ]