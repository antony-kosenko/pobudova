from django import forms

from core.models import Bill, Payment

METRIC_UNITS_CHOICES = (
    ("m3", "m3"),
    ("kw", "kW")
)


class BillForm(forms.ModelForm):
    """ Model form based on Bill model.
    Renders on template to represent a Bill model """

    unit = forms.ChoiceField(choices=METRIC_UNITS_CHOICES, required=False)

    class Meta:
        model = Bill
        fields = [
            "service_name",
            "date_due",
            "is_fixed_cost",
            "unit",
            "current_counter",
            "consumption",
            "cost_per_unit",
            "cost_due",
        ]

        labels = {
            "service_name": "Service Name",
            "unit": "Unit",
            "current_counter": "Counter",
            "consumption": "Consumed",
            "cost_per_unit": "Cost (per unit)",
            "cost_due": "Total Due",
        }

        widgets = {
            'service_name': forms.TextInput(attrs={'placeholder': 'e.g. Hot water'}),
            'date_due': forms.DateInput(format="%d/%m/%Y", attrs={'type': 'date'})
        }


class PaymentForm(forms.ModelForm):
    """ Model form based on Payment model.
    Represents the model with one field only."""
    class Meta:
        model = Payment
        fields = ('actual_payment',)
