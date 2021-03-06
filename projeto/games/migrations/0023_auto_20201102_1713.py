# Generated by Django 3.1.1 on 2020-11-02 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0022_auto_20201102_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('subtitle', models.CharField(max_length=180, null=True)),
                ('slug', models.CharField(max_length=240, null=True)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
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
