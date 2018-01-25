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
            'destiny':forms.CheckboxSelectMultiple(
                attrs={
                }
            ),
        }


