# Generated by Django 3.2.16 on 2023-12-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0017_alter_comment_page_number_by_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='sort',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сортировка'),
        ),
    ]
