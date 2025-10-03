from . models import Contact
from django import forms
class Contactforms(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['firstname','lastname','address','email','phone']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = Contact.objects.filter(email=email)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError("A contact with this email already exists.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            qs = Contact.objects.filter(phone=phone)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError("A contact with this phone number already exists.")
            if not phone.isdigit() or len(phone) != 10:
                raise forms.ValidationError("Enter a valid 10-digit phone number.")
        return phone


