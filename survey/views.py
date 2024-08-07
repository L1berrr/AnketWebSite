from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import SurveyResponse

def survey_page(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            SurveyResponse.objects.create(
                question1=data['question1'],
                question2=data['question2'],
                question3=data['question3'],
                question4=data['question4'],
                question5=data['question5'],
                question6=data['question6'],
                phone=data['phone']
            )
            return redirect('thank_you_page')
    else:
        form = SurveyForm()
    return render(request, 'survey/survey_page.html', {'form': form})

def admin_page(request):
    if not request.user.is_superuser:
        return redirect('login')
    responses = SurveyResponse.objects.all()
    return render(request, 'survey/admin_page.html', {'responses': responses})

def thank_you_page(request):
    return render(request, 'survey/thank_you_page.html')
