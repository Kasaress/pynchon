# Generated by Django 2.2.19 on 2022-10-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_auto_20221008_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='wiki/', verbose_name='Картинка'),
        ),
    ]
