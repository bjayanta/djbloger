from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "author", "content", "status", "created_at", "updated_at",)
    prepopulated_fields = {"slug": ("title", )}


# admin.site.register(Post)
admin.site.register(Post, PostAdmin)
