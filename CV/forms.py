from django import forms


class ContactUs(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    subject = forms.CharField(max_length=300
                              , widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    email = forms.CharField(max_length=100
                            , widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}))
