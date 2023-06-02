from django.contrib import admin
from .models import Discussion
# Register your models here.
@admin.register(Discussion)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}