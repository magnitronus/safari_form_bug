from django import forms

from mainapp.models import Something


class SomethingForm(forms.ModelForm):

    class Meta:
        model = Something
        fields = ('name', 'some_file', )
