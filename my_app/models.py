from django.db import models
from datetime import date


class Block(models.Model):
    number = models.CharField(max_length=100, verbose_name='Номер блока')
    price = models.IntegerField(verbose_name='Стоимость за квадратный метр')
    numb_entr = models.IntegerField(verbose_name='Количесвто подъездов')
    numb_floor = models.IntegerField(verbose_name='Количесвто этажей')
    numb_flat = models.IntegerField(verbose_name='Количесвто картир на этаже')

    def __str__(self):
        return self.number


class Flat(models.Model):
    status_choices = [
        ('Выкуп', 'Выкуп'),
        ('Выкуп не до конца', 'Выкуп не до конца'),
        ('Расторгнуто', 'Расторгнуто'),
        ('Не продано', 'Не продано'),
    ]
    name = models.TextField(blank=True, null=True, verbose_name='ФИО владельца')
    sale_date = models.IntegerField(blank=True, null=True, verbose_name='Дата продажи')
    status = models.CharField(max_length=100, choices=status_choices, verbose_name='Статус')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, verbose_name='Блок')
    tot_area = models.IntegerField(verbose_name='Общая площадь')

    def __str__(self):
        return self.status


