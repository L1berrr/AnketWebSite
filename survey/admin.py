from django.contrib import admin
from .models import SurveyResponse

@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'phone')
    search_fields = ('phone',)
