# Generated by Django 3.2.16 on 2023-12-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0015_alter_chapter_pov'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='page_number_by_2021',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Нумерация глав в новом издании'),
        ),
    ]
