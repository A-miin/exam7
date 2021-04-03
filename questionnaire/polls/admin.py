from django.contrib import admin
from .models import Poll, Choice

# Register your models here.
class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']
    fields = ['id', 'question', 'created_at']
    readonly_fields = ['id', 'created_at']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id','option']
    fields = ['id', 'option', 'poll']
    readonly_fields = ['id']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)

