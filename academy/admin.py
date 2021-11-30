from django.contrib import admin

from academy.models import Academy, Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'credits', 'price_per_credit', 'academy']
    list_editable = ['credits', 'price_per_credit', 'academy']
    list_per_page = 10
    search_fields = ['name']

@admin.register(Academy)
class AcademyAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']