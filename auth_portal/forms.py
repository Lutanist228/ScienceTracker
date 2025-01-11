from django import forms

class SaveStudProfile(forms.Form):
    group = forms.CharField(max_length=100)
    spec = forms.CharField(max_length=300)
    fac = forms.CharField(max_length=150)
    educ = forms.CharField(max_length=150)
    orcid = forms.CharField(max_length=100)
    interest = forms.CharField(max_length=300)

class SaveSupProfile(forms.Form): pass
