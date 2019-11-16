from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "istifadeci adi")
    password = forms.CharField(label = "parol",widget = forms.PasswordInput)
    
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label = "istifadeci adi")
    password = forms.CharField(max_length=50,label="parol",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=50,label = "parolu dogrula",widget=forms.PasswordInput)



    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("parollar eslesmir")

        values = {
            "username" : username ,
            "password" : password
        }    
        return values









