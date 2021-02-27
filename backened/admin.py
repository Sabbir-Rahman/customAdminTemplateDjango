from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html

from .models import test
from django.urls import path
from django.http import HttpResponseRedirect
admin.site.site_header = 'Admin Tutorial Dashboard'

class testAdmin(admin.ModelAdmin):
    list_display = ('title', 'created','font_size_html_display')
    list_filter = ('created',)
    menu_title = "Users"
    change_list_template = 'admin/test/test_change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('fontsize/<int:size>/', self.change_font_size)
        ]
        return custom_urls + urls

    def change_font_size(self, request, size):
        self.model.objects.all().update(font_size=size)
        self.message_user(request, 'font size set succesfully!')
        return HttpResponseRedirect("../")

    def font_size_html_display(self, obj):
        display_size = obj.font_size if obj.font_size <= 30 else 30
        return format_html(
            f'<span style="font-size: {display_size}px;">{obj.font_size}</span>'
        )

admin.site.register(test,testAdmin)
admin.site.unregister(Group)
