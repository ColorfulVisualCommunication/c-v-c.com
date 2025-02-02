from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'short_description', 'description', 'technologies', 'image', 'testemonial'] # The fields that we want to be displayed in the form