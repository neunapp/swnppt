from .models import User
from django import forms
from django.contrib.auth import authenticate

class UserAddForm(forms.ModelForm):
    """ formulario para registrar usuarios """

    password = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
            }
        ),
    )
    class Meta:
        model = User
        fields = (
            'email',
            'nacionality',
        )
        #
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres...',
                }
            ),

        }

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 5:
            print('menor a 5 caracteres')
            self.add_error(
                'password',
                'la contraseña debe tener por lo menos 5 caracteres!!'
            )
        else:
            return password



class UserLoginForm(forms.Form):
    """
        formuario para logear Usuario
    """

    email = forms.CharField(
        label='Email',
        max_length='100',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
                'name': 'email',
                'autofocus': 'autofocus',
            }
        ),
    )
    password = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
            }
        ),
    )
    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('email o password incorrectos.')
        return self.cleaned_data