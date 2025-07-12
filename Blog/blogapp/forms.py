from django import forms


class InputForm(forms.Form):
    username =forms.CharField(max_length=200)
    password =forms.CharField(widget=forms.PasswordInput)
    email =forms.EmailField()


class LoginForm(forms.Form):
    username = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")