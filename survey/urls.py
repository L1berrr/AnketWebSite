from django.urls import path
from .views import survey_page, admin_page, thank_you_page

urlpatterns = [
    path('', survey_page, name='survey_page'),
    path('admin/', admin_page, name='admin_page'),
    path('thank-you/', thank_you_page, name='thank_you_page'),
]
