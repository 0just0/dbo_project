from django.contrib import admin
from .models import Bank, Bank_Ul


class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'safe', 'info', 'service', 'add_service', 'investments', 'transfers', 'accounts', 'bank_contact', 'terminal_availability')
    search_fields = ('name',)


class BankUlAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'info', 'business_func', 'safe', 'bank_contact', 'currency_work')
    search_fields = ('name',)


admin.site.register(Bank, BankAdmin)
admin.site.register(Bank_Ul, BankUlAdmin)
