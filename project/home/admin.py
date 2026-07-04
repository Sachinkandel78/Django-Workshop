from django.contrib import admin
from .models import Student,School

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'phone']   #admin panel ma search wala option 
    list_filter = ['is_present']
    list_display = ['id', 'name','phone','course', 'age',]

admin.site.register(Student,StudentAdmin)
admin.site.register(School)
# Register your models here.

admin.site.site_header = "My Admin"
admin.site.site_title = "My Admin Portal"

admin.site.index_title = "Welcome to My Admin Portal"

