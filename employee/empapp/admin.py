from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id','name', 'designation', 'photo_preview')
    search_fields = ('name', 'designation')
    list_filter = ('designation',)

    def photo_preview(self, obj):
        if obj.photo:
            return '<img src="%s" width="100" />' % obj.photo.url
        else:
            return 'No photo'
    
    photo_preview.allow_tags = True
    photo_preview.short_description = 'Photo Preview'
