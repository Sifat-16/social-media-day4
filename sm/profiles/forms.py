from django import forms
from .models import Profile

CHI = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class ProfileForm(forms.ModelForm):
    interest = forms.ChoiceField(widget=forms.RadioSelect, choices=CHI)
    class Meta:
        
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'bio', 'country', 'profession', 'interest', 'language']

        widgets = {
            'first_name': forms.TextInput(attrs={'type': 'text', 'id': 'input', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'type': 'text', 'id': 'input', 'required': 'required'}),
            
            'interest': forms.TextInput(attrs={'type': 'radio', 'checked': 'checked', 'name': 'radio'}),
            'country': forms.TextInput(attrs={'type': 'text', 'id': 'input', 'required': 'required'}),
            'bio': forms.Textarea(attrs={'rows': '4', 'id': 'textarea', 'required': 'required'}),
            'profession': forms.TextInput(attrs={'type': 'text', 'id': 'input', 'required': 'required'}),
            'language': forms.TextInput(attrs={'type': 'text', 'id': 'input', 'required': 'required'}),
            
        }


class ProfilePic(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']


class CoverPic(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['cover_pic']
