# Generated by Django 3.1.1 on 2020-10-30 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20201029_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogos',
            name='genero',
        ),
        migrations.AddField(
            model_name='generos',
            name='games',
            field=models.ManyToManyField(blank=True, related_name='generos', to='games.Jogos'),
        ),
    ]
