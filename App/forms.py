from django import forms
from App.models import Company, Feedback
from django.contrib.auth.models import User


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

class FeedbackForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=100)
    comment = forms.CharField(max_length=100)


class EmployeeCreateForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(widget = forms.PasswordInput(), max_length=100)

class EmployeeEditForm(forms.ModelForm):
    password = forms.CharField(required = False, widget = forms.PasswordInput(), max_length=100,
       help_text = "If you dont wish to change the users password leave the form blank or fill it to change a users password")
    class Meta:
        model = User
        fields = [ 'username','last_name', 'password']
