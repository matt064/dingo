from django import forms
from maths.models import Result, Math

class ResultForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        value = cleaned_data.get('value')
        error = cleaned_data.get('error')

        if value and error:
            raise forms.ValidationError("Podaj tylko jedną z wartości")
        elif not (value or error):
            raise forms.ValidationError("Nie podano żadnej wartości!")


    class Meta:
        model = Result
        fields = "__all__"


# class MathForm(forms.ModelForm):

#     def clean(self):
#         cleaned_data = super().clean()
#         operation = cleaned_data.get('operation')
#         a = cleaned_data.get('a')
#         b = cleaned_data.get('b')

#     class Meta:
#         model = Math
#         fields 