from django.contrib import admin
from .models import News


# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "context","get_image"]
    search_fields = ["title","context"]
    readonly_fields = ["get_image"]



admin.site.register(News, NewsAdmin)
