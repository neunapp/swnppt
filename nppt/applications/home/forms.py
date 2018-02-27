from django import forms


from .models import ContactUs


class ContactUsForm(forms.ModelForm):

    ESTRELLA_5 = '3'
    ESTRELLA_4 = '2'
    ESTRELLA_3 = '1'
    ECONOMY = '0'

    MODE_CHOICES = (
        (ESTRELLA_5, '5 star'),
        (ESTRELLA_4, '4 star'),
        (ESTRELLA_3, '3 star'),
        (ECONOMY, 'Economy'),
    )

    COMPARTIDO = '2'
    PRIVADO = '1'
    MODE_CHOICES_HOTEL = (
        (PRIVADO, 'privado'),
        (COMPARTIDO, 'compartido'),

    )


    class Meta:

        destiny = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            required=True,
            queryset=ContactUs.objects.all()
        )

        model = ContactUs
        fields = (
            'name',
            'last_name',
            'email',
            'phone',
            'skype',
            'best_time_contact',
            'country_residence',
            'city',
            'destiny',
            'departure_date',
            'days_amount',
            'adult_amount',
            'infant_amount',
            'boy_infant_amount',
            'boy_amount',
            'hotel',
            'type_service',
            'message',
        )

        widgets = {
            'name':forms.TextInput(
                attrs={
                    'placeholder':'Nombres',
                    'class':'simple-form',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Apellidos',
                    'class':'simple-form',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'E-mail',
                    'class':'simple-form',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Telefono',
                    'class':'simple-form',
                }
            ),
            'skype': forms.TextInput(
                attrs={
                    'placeholder': 'skype',
                    'class':'simple-form',
                }
            ),
            'best_time_contact': forms.TextInput(
                attrs={
                    'placeholder': 'Mejor momento para contactar',
                    'class':'simple-form',
                }
            ),
            'country_residence': forms.TextInput(
                attrs={
                    'placeholder': 'País de residencia',
                    'class':'simple-form',
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'ciudad',
                    'class':'simple-form',
                }
            ),
            'destiny': forms.Select(
                attrs={
                    'placeholder': 'Destino favorito',
                    'class':'simple-form',
                }
            ),
            'departure_date': forms.DateInput(
                attrs={
                    'class':'simple-form',
                    'type':'date',
                }
            ),
            'days_amount': forms.NumberInput(
                attrs={
                    'placeholder': 'cantidad de dias',
                    'class':'simple-form',
                }
            ),
            'adult_amount': forms.NumberInput(
                attrs={
                    'placeholder': 'adultos',
                    'class':'simple-form',
                }
            ),
            'infant_amount': forms.NumberInput(
                attrs={
                    'placeholder': 'infantes(0-24 meses)',
                    'class':'simple-form',
                }
            ),
            'boy_infant_amount': forms.NumberInput(
                attrs={
                    'placeholder': 'niños (2-5 años)',
                    'class':'simple-form',
                }
            ),
            'boy_amount': forms.NumberInput(
                attrs={
                    'placeholder': 'niños de 12 años ',
                    'class':'simple-form',
                }
            ),
            'hotel': forms.Select(
                attrs={
                    'placeholder': 'hotel',
                    'class':'simple-form',
                }
            ),
            'type_service': forms.Select(
                attrs={
                    'placeholder': 'tipo de servicio',
                    'class':'simple-form',
                }
            ),
            'message':forms.Textarea(
                attrs={
                    'placeholder': 'mensaje',
                    'class':'simple-form',
                    'rows':'4',
                }
            )
        }
