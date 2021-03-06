from django.contrib import admin

from academy.models import Academy, Student, Subject

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

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone']
    search_fields = ['first_name', 'last_name']
    list_per_page = 10
    
    @admin.display(ordering='first_name')
    def full_name(self, student: Student):
        return student.first_name + ' ' + student.last_name