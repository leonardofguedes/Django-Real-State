from django.contrib import admin
from .models import Imovel, Category

class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Imovel)

class ImovelAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)