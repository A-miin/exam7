from django.contrib import admin
from .models import Poll, Choice, Answer

# Register your models here.
class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']
    fields = ['id', 'question', 'created_at']
    readonly_fields = ['id', 'created_at']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id','option']
    fields = ['id', 'option', 'poll']
    readonly_fields = ['id']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll', 'choice']
    fields = ['id', 'poll', 'choice', 'created_at']
    readonly_fields = ['id', 'created_at']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
