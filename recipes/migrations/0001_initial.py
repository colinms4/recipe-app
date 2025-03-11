# Generated by Django 4.2.19 on 2025-03-11 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('ingredients', models.TextField()),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=50)),
                ('cooking_time', models.IntegerField(help_text='Cooking time in minutes')),
            ],
        ),
    ]
