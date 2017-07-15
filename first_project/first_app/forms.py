from django import forms
from django.core import validators
from first_app.models import db_users


# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name needs to start with z")


class FormPage(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter Your Email Again')
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure Emails Match!")
    #
    #
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0 :
    #         raise forms.ValidationError("Botchtcher Validation Error!")
    #     return botcatcher

class CreateUser(forms.ModelForm):

    class Meta:
        model = db_users
        fields = '__all__'



from django import forms
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
