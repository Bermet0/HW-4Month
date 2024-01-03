from django import forms

import parser_app.parser_litres
from . import models


class ParserForm(forms.Form):
    MEDIA_CHOICES = ("litres.ru", 'litres.ru')
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ['media_type']

    def parser_data(self):
        if self.cleaned_data['media_type'] == 'litres.ru':
            book_parser = parser_app.parser_litres.parser_litres()
            for i in book_parser:
                models.LitresModel.objects.create(**i)
