from django import forms
from .models import TodoModel


class NoutbookForm(forms.ModelForm):
    noutbook_name_uz = forms.CharField()
    noutbook_name_en = forms.CharField()
    noutbook_name_ru = forms.CharField()

    information_uz = forms.CharField()
    information_en = forms.CharField()
    information_ru = forms.CharField()

    class Meta:
        model = TodoModel
        exclude = ('noutbook_name', 'information')