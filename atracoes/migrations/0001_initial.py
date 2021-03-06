# Generated by Django 2.0.4 on 2019-04-28 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('horario_func', models.TextField()),
                ('idade_minima', models.ImageField(upload_to='')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='atracoes')),
                ('observacoes', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
