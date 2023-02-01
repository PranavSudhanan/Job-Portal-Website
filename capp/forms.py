from django import forms
from django.contrib.auth.models import User


class regform(forms.Form):
    companyname = forms.CharField(max_length=25)
    email = forms.EmailField()
    password = forms.CharField(max_length=20)
    cpassword = forms.CharField(max_length=20)
    number = forms.IntegerField()
    address = forms.CharField(max_length=100)

class logform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

class upform(forms.Form):
    cname = forms.CharField(max_length=50)
    email = forms.EmailField()
    jtitle = forms.CharField(max_length=25)
    jtype = forms.CharField(max_length=25)
    wtype = forms.CharField(max_length=25)
    exp = forms.CharField(max_length=25)
    qualify = forms.CharField(max_length=70)

class uform(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ulogform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

class userprofileform(forms.Form):
    image = forms.ImageField()
    fname = forms.CharField(max_length=25)
    email = forms.EmailField()
    resume = forms.FileField()
    qualify = forms.CharField(max_length=70)
    exp = forms.CharField(max_length=25)
    address = forms.CharField(max_length=200)
    phone = forms.IntegerField()

class jobapplyform(forms.Form):
    cname = forms.CharField(max_length=50)
    jtitle = forms.CharField(max_length=50)
    fname = forms.CharField(max_length=50)
    email = forms.EmailField()
    resume = forms.FileField()

class emailform(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(max_length=100)

