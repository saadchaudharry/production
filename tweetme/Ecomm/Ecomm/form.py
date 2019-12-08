from django import forms

class Contactname(forms.Form):
    Fullname  =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    Email     =forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
    content   =forms.CharField(max_length=120,widget=forms.Textarea(attrs={"class":"form-control"}))


    def clean_Email(self):
        Email=self.cleaned_data.get("Email")
        if not "@" in Email:
            raise forms.ValidationError("Enter a proper email address")
        return Email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
