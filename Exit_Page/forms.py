from django import forms

def UserForm(forms.ModelForm):
    class Meta:
        model = UserInformations
        exclude = [""]
