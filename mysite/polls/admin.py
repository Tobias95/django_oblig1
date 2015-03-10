from django.contrib import admin
from polls.models import Question
from polls.models import Choice, Question
# ...
admin.site.register(Choice)


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(Question, QuestionAdmin)