from django import forms


class BankForm(forms.Form):
    price = forms.ChoiceField(('Price'))
    safe = forms.ChoiceField(('Safe'))
    info = forms.ChoiceField(('Info'))
    service = forms.ChoiceField(('Service'))
