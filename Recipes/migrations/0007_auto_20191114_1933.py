# Generated by Django 2.2.7 on 2019-11-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0006_auto_20191114_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favourite_recipes',
            field=models.ManyToManyField(blank=True, related_name='favourite_recipes', to='Recipes.Recipe'),
        ),
    ]
