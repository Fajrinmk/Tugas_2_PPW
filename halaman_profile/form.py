from django import forms
from .views import birthdate, gender, email,desc_profile,expert,profile_name
from .models import DataProfile

class edit_profile_form(forms.Form):
    profile = DataProfile.objects.get(pk=1)

    error_messages = {
        'required': 'Tolong isi input ini',
    }
    nama_attrs = {
        'type': 'text',
        'class': 'edit-nama-input',
        'initial' : profile.name
    }
    gender_attrs = {
        'type': 'text',
        'class': 'edit-nama-input',
        'initial' : profile.name
    }
    birthdate_attrs = {
        'type': 'text',
        'class': 'edit-ttl-textarea',
        'initial' : profile.birthday
    }
    email_attrs = {
        'type': 'text',
        'class': 'edit-email-textarea',
        'initial' : profile.email
    }
    expertise_attrs = {
        'type': 'text',
        'class': 'edit-ttl-textarea',
        'initial' : profile.expertise
    }
    profile_image_attrs = {
        'type': 'text',
        'class': 'edit-link-textarea',
        'placeholder':'insert link'
    
    }
      npm_attrs = {
        'type': 'text',
        'class': 'edit-link-textarea',
        'placeholder': profile.npm
        }
    description_attrs = {
        'type': 'text',
        'cols': 50,
        'rows': 4,
        'class': 'todo-desc-textarea',
        'initial' : profile.description
    }

    nama = forms.CharField(label='', required=True, max_length=27, widget=forms.TextInput(attrs=nama_attrs))

    npm = forms.CharField(label='', required=True, max_length=27, widget=forms.TextInput(attrs=npm_attrs))
    birthdate = forms.CharField(label='', required=True, max_length=27, widget=forms.TextInput(attrs=birthdate_attrs))
    gender = forms.CharField(label='', required=True, max_length=27, widget=forms.TextInput(attrs=gender_attrs))
    email = forms.CharField(label='', required=True, max_length=27, widget=forms.TextInput(attrs=email_attrs))
    profile_image = forms.CharField(label='', required=True, max_length=27, widget=forms.URLInput(attrs=profile_image_attrs))
    expertise = forms.CharField(label='', required=True, max_length=27, widget=forms.CheckBox(attrs=expertise_attrs))
    description = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=descriptions_attrs))