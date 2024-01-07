from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER_TYPE = (
    ("MALE", "M"),
    ("FEMALE", 'Ж'),
    ('UNDEFINED', 'Нет')
)

CITY_TYPE = (
    ("KG", "Кыргызстан"),
    ("KZ", "Казахстан"),
    ("RUS", "Россия"),
    ("USA", "Америка"),
    ("CN", "Китай"),
)


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, initial='+996', label='Укажите номер телефона')
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    city = forms.ChoiceField(choices=CITY_TYPE)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'date_of_birth',
            'gender',
            'city'
        )

    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
