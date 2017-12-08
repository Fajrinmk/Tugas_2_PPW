from django import forms

class Status_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
        
    }
    status_attrs = {
        'type': 'text',
        'cols' : 149,
        'rows' : 4,
        'class' : 'status-form-input',
        'placeholder' : 'Apa yg anda pikirkan?'
    }

   
    status = forms.CharField(label='',widget=forms.Textarea(attrs=status_attrs), required=True)