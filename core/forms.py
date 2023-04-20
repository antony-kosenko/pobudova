from django.forms import ModelForm, DateField, ChoiceField
from django_flatpickr.widgets import DatePickerInput

from core.models import Bill, Payment

METRIC_UNITS_CHOICES = (
    ("m3", "m3"),
    ("kw", "kW")
)


class BillForm(ModelForm):
    unit = ChoiceField(choices=METRIC_UNITS_CHOICES, required=False)
    date_due = DateField(widget=DatePickerInput(), required=True)

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

    # def clean(self):
    #     # TODO To be simplified (Looks like not working)
    #     super().clean()
    #     if not self.fixed_cost:
    #         if not self.unit:
    #             raise ValidationError({'unit': 'This field is required.'})
    #         if not self.current_counter:
    #             raise ValidationError({'current_counter': 'This field is required.'})
    #         if not self.cost_per_unit:
    #             raise ValidationError({'cost_per_unit': 'This field is required.'})


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ('actual_payment',)
