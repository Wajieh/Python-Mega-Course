from django.contrib import admin
from .models import Form
# Register your models here.


class FormAdmin(admin.ModelAdmin):
    
    list_display = ("firstname", "lastname", "email")
    search_fields = ("firstname", "lastname", "email")
    list_filter = ("date", "occupation")
    ordering = ("firstname", )
    readonly_fields = ("occupation",)
admin.site.register(Form,FormAdmin)

