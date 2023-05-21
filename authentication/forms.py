from django import forms
class ReviewForm(forms.Form):
    user_name= forms.CharField(error_messages={
        "required": "Your name cannot be empty!!"
    },max_length=100, widget=forms.TextInput(attrs={'class': "field", 'placeholder':"Full Name"})) 
    phone_number= forms.IntegerField(error_messages={
        "required": "Your name cannot be empty!!"
    }, widget=forms.TextInput(attrs={'class': "field", 'placeholder':"Phone Number"})) 
    email= forms.EmailField(widget=forms.TextInput(attrs={'class': "field", 'placeholder':"Email"}))
    password= forms.CharField(max_length=16,min_length=8,widget=forms.PasswordInput(attrs={'class': "field", 'placeholder':"Password"}))