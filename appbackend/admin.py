from django.contrib import admin
from .models import User, Category, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', "__str__",)
    readonly_fields = ('id',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', "__str__",)
    readonly_fields = ('id',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', "__str__",)
    readonly_fields = ('id',)

