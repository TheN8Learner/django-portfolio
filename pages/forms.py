from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        labels = {
            "name": "Nom",
            "email": "Email",
            "message": "Message",
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Ton nom",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "tonemail@example.com",
            }),
            "message": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Écris ton message ici...",
            }),
        }