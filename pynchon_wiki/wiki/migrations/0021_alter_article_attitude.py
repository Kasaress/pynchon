# Generated by Django 3.2.16 on 2024-03-27 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0020_alter_tablechronology_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='attitude',
            field=models.TextField(choices=[('Другое', 'Другое'), ('Раздел 1', 'Раздел 1'), ('V Раздел 1', 'V Раздел 1'), ('Раздел 4', 'Раздел 4'), ('V Раздел 4', 'V Раздел 4'), ('V Раздел 5', 'V Раздел 5'), ('Раздел 1 (статья 1)', 'Раздел 1 (статья 1)'), ('V Раздел 3', 'V Раздел 3'), ('Раздел 1 (статья 2)', 'Раздел 1 (статья 2)'), ('Раздел 5', 'Раздел 5'), ('Раздел 7', 'Раздел 7'), ('Авторы', 'Авторы'), ('Томас Пинчон', 'Томас Пинчон'), ('Запланированные мероприятия', 'Запланированные мероприятия'), ('Записи встреч', 'Записи встреч'), ('Другие книги', 'Другие книги'), ('О сайте', 'О сайте')], verbose_name='Отношение к разделу'),
        ),
    ]
