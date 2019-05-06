from django.contrib import admin
from sign.models import Event, Guest


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']  # 用于定义要在列表中显示哪些字段，当然，这些字段名称必须是模型中的Event()类所定义的
    search_fields = ['name']  # 搜索栏
    list_filter = ['status']  # 过滤器


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    search_fields = ['realname', 'phone']  # 搜索栏
    list_filter = ['sign']  # 过滤器


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
