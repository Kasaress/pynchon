# Generated by Django 2.2.19 on 2022-10-08 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0008_auto_20221008_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка'),
        ),
    ]
