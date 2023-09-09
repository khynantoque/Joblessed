from django.contrib import admin
from app.models import JobPost

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'date')
    list_filter = ('date', 'salary', 'expiry')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'salary')
        }),
        ('Additional Information', {
            'classes': ('collapse',),
            'fields': ('expiry', 'slug')
        }),
    )

# Register your models here.
admin.site.register(JobPost, JobAdmin)
admin.site.site_header = 'JoBlessed Admin'
admin.site.site_title = 'JobBlessed Portal'
admin.site.index_title = 'Welcome user!'