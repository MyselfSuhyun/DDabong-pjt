# Generated by Django 3.2.9 on 2021-11-24 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='movies',
            field=models.ManyToManyField(blank=True, related_name='my_keywords', to='movies.Movie'),
        ),
    ]
