# Generated by Django 3.1.1 on 2020-11-02 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0024_auto_20201102_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='games',
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
