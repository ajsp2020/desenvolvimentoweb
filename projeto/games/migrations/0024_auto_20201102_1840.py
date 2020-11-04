# Generated by Django 3.1.1 on 2020-11-02 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0023_auto_20201102_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='games',
            field=models.ManyToManyField(blank=True, related_name='blogpost', to='games.Jogos'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(blank=True, max_length=240, null=True),
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
