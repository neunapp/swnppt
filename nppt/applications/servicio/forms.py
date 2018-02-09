from django import forms


class SearchServiceForm(forms.Form):
    '''
    formulario para buscar servicios
    '''

    kword = forms.CharField(
        max_length='300',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'search__input__1',
                'placeholder': 'Buscar..'
            }
        )
    )
