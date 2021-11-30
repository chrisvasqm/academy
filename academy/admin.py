from django.contrib import admin

from academy.models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'credits', 'price_per_credit']
    list_editable = ['credits', 'price_per_credit']
    list_per_page = 10
    search_fields = ['name']