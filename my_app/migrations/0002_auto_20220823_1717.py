# Generated by Django 3.2 on 2022-08-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='sale_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата продажи'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='tot_area',
            field=models.IntegerField(verbose_name='Общая площадь'),
        ),
    ]
