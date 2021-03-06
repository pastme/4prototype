# Generated by Django 2.2.2 on 2019-06-27 12:55

import books.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True)),
                ('isbn', models.CharField(max_length=13, validators=[books.validators.ISBNValidator])),
                ('categories', models.ManyToManyField(to='categories.Category')),
            ],
            options={
                'verbose_name_plural': 'books',
            },
        ),
    ]
