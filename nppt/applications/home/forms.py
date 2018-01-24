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
"""
        widgets = {
            'name':forms.TextInput(
                attrs={
                    'placeholder':'nombre',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'apellido',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'correo',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Telefono',
                }
            ),
            'skype': forms.TextInput(
                attrs={
                    'placeholder': 'skype',
                }
            ),
            'best_time_contact': forms.TextInput(
                attrs={
                    'placeholder': 'mejor momento para contactar',
                }
            ),
            'country_residence': forms.TextInput(
                attrs={
                    'placeholder': 'pais de residencia',
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'ciudad',
                }
            ),
            'destiny': forms.TextInput(
                attrs={
                    'placeholder': 'nombre',
                }
            ),
            'departure_date': forms.TextInput(
                attrs={
                    'placeholder': 'fecha de partida',
                }
            ),
            'days_amount': forms.TextInput(
                attrs={
                    'placeholder': 'cantidad de dias',
                }
            ),
            'adult_amount': forms.TextInput(
                attrs={
                    'placeholder': 'adultos',
                }
            ),
            'infant_amount': forms.TextInput(
                attrs={
                    'placeholder': 'infantes(0-24 meses)',
                }
            ),
            'boy_infant_amount': forms.TextInput(
                attrs={
                    'placeholder': 'niños (2-5 años)',
                }
            ),
            'boy_amount': forms.TextInput(
                attrs={
                    'placeholder': 'niños de 12 años ',
                }
            ),
            'hotel': forms.TextInput(
                attrs={
                    'placeholder': 'hotel',
                }
            ),
            'type_service': forms.TextInput(
                attrs={
                    'placeholder': 'tipo de servicio',
                }
            ),
            'message':forms.Textarea(
                attrs={
                    'placeholder': 'mensaje'
                }
            )


        }"""
