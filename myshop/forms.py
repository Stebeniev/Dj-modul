from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from myshop.models import MyUser, Purchase, Return


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Your Username:', widget=forms.TextInput)
    password1 = forms.CharField(label='Your Password:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password:', widget=forms.PasswordInput)
    cash = forms.DecimalField(initial=10000, widget=forms.HiddenInput)

    class Meta:
        model = MyUser
        fields = ('username', 'password1', 'password2', 'cash')

    def clean(self):
        username = self.cleaned_data.get('username')
        if MyUser.objects.filter(username=username).exists():
            raise ValidationError('User with this name exists')


class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('product_id', 'quantity')


class ReturnCreateForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ('delete_id',)


