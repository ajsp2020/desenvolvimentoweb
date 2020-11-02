# Generated by Django 3.1.1 on 2020-11-02 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0025_auto_20201102_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='nome',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='games.jogos'),
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
    ]
