from django.contrib import admin
from myblog.models import post

# Register your models here.
class post_table (admin.ModelAdmin):
    list_display = ["postDate","postTitle","postNote"]
admin.site.register(post,post_table)