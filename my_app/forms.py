from django import forms
from my_app import models
from django.contrib.auth.admin import User

#create your forms here

class product_add(forms.ModelForm):
    class Meta:
        model = models.products
        fields = "__all__"

class accounter(forms.ModelForm):
    username = forms.CharField(help_text=False)
    password = forms.CharField(widget=forms.PasswordInput())
    Confirm_Password = forms.CharField(widget=forms.PasswordInput())
    
    
    def clean(self):
        all_data = super().clean()
        if(all_data["password"] != all_data["Confirm_Password"]):

            raise forms.ValidationError("Password Not Correct")

    class Meta:
        model = User
        fields = ('username','email','password')