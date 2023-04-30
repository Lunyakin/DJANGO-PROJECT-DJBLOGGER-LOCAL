from typing import Any, Mapping, Optional, Type, Union
from django import forms
from django.forms.utils import ErrorList


class PostSearchForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwars):
        super().__init__(*args, **kwars)
        self.fields['q'].widget.attrs.update({'class': 'form-control'})