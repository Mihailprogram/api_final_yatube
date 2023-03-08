# Generated by Django 3.2.16 on 2023-03-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230305_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL группы')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
