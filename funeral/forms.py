from django import forms
from taggit.forms import TagWidget, TagField
from .models import Funeral


class FuneralForm(forms.ModelForm):
    name = forms.CharField(label='اسم المتوفي',
                           widget=forms.TextInput(attrs={'placeholder': 'اسم المتوفي', 'class': 'form-control'}),
                           error_messages={'required': 'يجب كتابة اسم المتوفي'})
    body = forms.CharField(label='بيانات صلاة الجنازة والدفن',
                           widget=forms.Textarea(
                               attrs={'placeholder': 'بيانات صلاة الجنازة والدفن', 'class': 'form-control', 'rows': '8',
                                      'cols': '40'}),
                           error_messages={'required': 'يجب كتابة بيانات الصلاة والدفن'})
    place_tags = TagField(label='هاشتاق المكان: مثال  (اليمن, حضرموت, الشحر)',
                                 widget=TagWidget(
                                     attrs={'placeholder': 'افصل بين اﻻسماء بفاصلة (,)', 'class': 'form-control'}),
                                 error_messages={'required': 'يجب كتابة مكان الصلاة والدفن'})

    class Meta:
        model = Funeral
        fields = ['name', 'body', 'place_tags']
