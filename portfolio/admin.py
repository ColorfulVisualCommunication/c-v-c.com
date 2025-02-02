from django.contrib import admin
from .models import Portfolio

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin): # This class will allow us to customize the admin interface for our Portfolio model
    list_display = ('title', 'short_description', 'created_at')
    search_fields = ('title', 'technologies')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


admin.site.register(Portfolio, PortfolioAdmin)

# Customize the admin site header and title
admin.site.site_header = "Colourful Visual Communication Super Admin"
admin.site.site_title = "CVC Super Admin Portal"
admin.site.index_title = "Welcome to the CVC Super Admin Portal"