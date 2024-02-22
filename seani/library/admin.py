from django.contrib import admin

from .models import Module, Question

@admin.register(Question)
class QuesgtionAdmin(admin.ModelAdmin):
    list_display = ['pk','question_text', 'module', 'correct']
    list_filter = ['module']


class QuesgtionInline(admin.StackedInline):
    model = Question

# Register your models here.
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'num_questions']
    inlines = [QuesgtionInline]


