from django import forms

from .models import FrequentQestions


class SearchForm(forms.Form):
    '''
    formulario para buscar notas
    '''

    kword = forms.CharField(
        max_length='300',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'search-form__input',
                'placeholder': 'Buscar..'
            }
        )
    )


class FrequentQestionsForm(forms.ModelForm):
    """
    formulario para Preguntas frecuentes
    """

    class Meta:
        model = FrequentQestions
        fields = (
            'email',
            'question',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class':'form-banner__input',
                    'placeholder': 'E-mail',
                }
            ),
            'question': forms.Textarea(
                attrs={
                    'class':'form-banner__input',
                    'placeholder': 'Pregunta...',
                    'rows': '1',
                }
            ),
        }
