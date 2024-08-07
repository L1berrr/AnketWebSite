from django.db import models

class SurveyResponse(models.Model):
    question1 = models.CharField(max_length=10)
    question2 = models.CharField(max_length=10)
    question3 = models.CharField(max_length=10)
    question4 = models.CharField(max_length=10)
    question5 = models.CharField(max_length=10)
    question6 = models.CharField(max_length=10)
    phone = models.CharField(max_length=16, default='')

    def __str__(self):
        return f"Response {self.id} - {self.phone}"
