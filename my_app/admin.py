from django.contrib import admin
from .models import *


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_filter = ('block', 'status')
    # date_hierarchy = 'sale_date'
    search_fields = ('flat__name', )
    list_display = ('name', 'sale_date', 'status', 'tot_area', 'get_area')
    empty_value_display = 'без хоз'
    list_editable = ('sale_date',)

    @admin.display(description='Общая стоимость')
    def get_area(self, obj):
        return obj.tot_area * obj.block.price


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('number', 'numb_entr', 'numb_floor', 'numb_flat', 'get_flat', 'get_full_price')

    @admin.display(description='Общее количество квартир')
    def get_flat(self, obj):
        return obj.numb_floor * obj.numb_flat

    @admin.display(description='Итоговая стоимость всех квартир в блоке')
    def get_full_price(self, obj):
        return (obj.numb_floor * obj.numb_flat) * obj.price

