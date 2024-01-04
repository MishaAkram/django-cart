# cart/forms.py
from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, widget=forms.TextInput(attrs={'size': '2', 'value': '1', 'class': 'quantity', 'maxlength': '5'}), required=True)
    product_id = forms.IntegerField(widget=forms.HiddenInput(), required=True)
