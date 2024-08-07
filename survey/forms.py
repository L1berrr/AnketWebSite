from django import forms

class SurveyForm(forms.Form):
    QUESTION_CHOICES = [
        ('yes', 'Ha (Ҳа)'),
        ('no', 'Yo\'q (Йўқ)'),
    ]
    
    QUESTION2_CHOICES = [
        ('excellent', 'Ajoyib (Ажойиб)'),
        ('bad', 'Yomon (Ёмон)'),
    ]

    question1 = forms.ChoiceField(
        choices=QUESTION_CHOICES, 
        widget=forms.RadioSelect, 
        label="Haydovchining muomalasi sizga yoqdimi? (Ҳайдовчининг муомаласи сизга ёқдими?)"
    )
    question2 = forms.ChoiceField(
        choices=QUESTION2_CHOICES, 
        widget=forms.RadioSelect, 
        label="Mashinaning tozaligiga baho bering. (Машинанинг тозалигига баҳо беринг.)"
    )
    question3 = forms.ChoiceField(
        choices=QUESTION_CHOICES, 
        widget=forms.RadioSelect, 
        label="Haydovchi sizga xizmat doirasidan tashqari gapirdimi? (Ҳайдовчи сизга хизмат доирасидан ташқари гапирдими?)"
    )
    question4 = forms.ChoiceField(
        choices=QUESTION_CHOICES, 
        widget=forms.RadioSelect, 
        label="Haydovchi siz aytgan yo‘ldan yurdimi? (Ҳайдовчи сиз айтган йўлдан юрдими?)"
    )
    question5 = forms.ChoiceField(
        choices=QUESTION_CHOICES, 
        widget=forms.RadioSelect, 
        label="Haydovchi buyurtmangizni manzilingizga yetib borib tugatdimi? (Ҳайдовчи буюртмангизни манзилингизга етиб бориб тугатдими?)"
    )
    question6 = forms.ChoiceField(
        choices=QUESTION_CHOICES, 
        widget=forms.RadioSelect, 
        label="Haydovchi telefonda ko‘rsatilgan summani oldimi? (Ҳайдовчи телефонда кўрсатилган суммани олдими?)"
    )
    phone = forms.CharField(
        max_length=16, 
        widget=forms.TextInput(attrs={
            'class': 'form-control phone-input', 
            'placeholder': 'Telefon raqami', 
            'type': 'text',
            'pattern': r'[0-9+#%]*',
            'inputmode': 'numeric'
        }), 
        label="Telefon raqami"
    )
