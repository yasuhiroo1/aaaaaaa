from django import forms


class TopForm(forms.Form):
    name = forms.CharField(label = "名前")