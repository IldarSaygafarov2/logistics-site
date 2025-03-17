from django import forms

from .models import RequestMessage


class RequestMessageForm(forms.ModelForm):
    class Meta:
        model = RequestMessage
        fields = ["first_name", "email", "subject", "message"]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ваше имя"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Ваш email"}
            ),
            "subject": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Тема"}
            ),
            "message": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Сообщение"}
            ),
        }
