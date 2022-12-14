# Generated by Django 2.2.19 on 2022-10-31 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0017_chapter_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableChronology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, verbose_name='Дата')),
                ('description', models.TextField(verbose_name='Событие')),
            ],
            options={
                'verbose_name': 'Строка таблицы хронологии',
                'verbose_name_plural': 'Строки таблицы хронологии',
            },
        ),
    ]
