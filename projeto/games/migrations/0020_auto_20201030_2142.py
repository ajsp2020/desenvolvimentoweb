# Generated by Django 3.1.1 on 2020-10-31 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0019_auto_20201030_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desenvolvedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desenvolvedor', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='generos',
            name='games',
            field=models.ManyToManyField(blank=True, related_name='generos', to='games.Jogos'),
        ),
        migrations.AlterField(
            model_name='plataformas',
            name='games',
            field=models.ManyToManyField(blank=True, related_name='plataformas', to='games.Jogos'),
        ),
        migrations.AlterField(
            model_name='jogos',
            name='desenvolvedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.desenvolvedores'),
        ),
    ]
