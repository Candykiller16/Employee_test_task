from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import EmployeeMPTT


@admin.action(description='Reset to zero selected employees')
def reset_to_zero(modeladmin, request, queryset):
    queryset.update(paid_salary_inf=0)


@admin.register(EmployeeMPTT)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'role', 'parent_link', 'salary_amount', 'paid_salary_inf']
    list_display_links = ['full_name', 'parent_link']
    list_filter = ['role', 'level']
    actions = [reset_to_zero]

    def parent_link(self, obj):
        if obj.parent:
            return format_html("<a href='/admin/employees/employeemptt/{number}/change'>{obj}</a>", number=obj.parent_id,
                               obj=obj.parent)
        else:
            return None

    parent_link.allow_tags = True
    parent_link.admin_order_field = 'parent'
    parent_link.short_description = 'superior head'