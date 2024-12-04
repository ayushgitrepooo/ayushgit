from django.contrib import admin
from.models import Calculation

@admin.register(Calculation)
class CalculationAdmin(admin.ModelAdmin):
    list_display = ('num1', 'operation', 'num2', 'result', 'created_at')
    list_filter = ('operation', 'created_at')  
    search_fields = ('num1', 'num2', 'result') 
    ordering = ('-created_at',)  