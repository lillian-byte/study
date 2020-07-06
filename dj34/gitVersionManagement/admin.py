from django.contrib import admin
from gitVersionManagement.models import GitVersion,GitCategory


class GitVersionAdmin(admin.ModelAdmin):
    list_display = ['func','command','comment']
    list_display_links = ['command']
    list_filter=['cate']
    list_editable = ['comment']
    search_fields = ['func']




# Register your models here.
admin.site.register(GitVersion,GitVersionAdmin)
admin.site.register(GitCategory)
