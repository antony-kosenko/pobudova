from django.forms import ModelForm, ChoiceField, DateInput, DateField

from core.models import Bill, Payment

METRIC_UNITS_CHOICES = (
    ("m3", "m3"),
    ("kw", "kW")
)


class DatePicker(DateInput):  # datepicker class as widget
    input_type = 'date'


class BillForm(ModelForm):
    """ Model form based on Bill model.
    Renders on template to represent a Bill model """

    unit = ChoiceField(choices=METRIC_UNITS_CHOICES)
    date_due = DateField(widget=DatePicker)

    class Meta:
        model = Bill
        fields = "__all__"
        labels = {
            "service_name": "Service Name",
            "unit": "Unit",
            "current_counter": "Counter",
            "consumption": "Consumed",
            "cost_per_unit": "Cost (per unit)",
            "cost_due": "Total Due",
            "is_paid": "Closed"
        }


class PaymentForm(ModelForm):
    """ Model form based on Payment model.
    Represents the model with one field only."""
    class Meta:
        model = Payment
        fields = ('actual_payment',)
