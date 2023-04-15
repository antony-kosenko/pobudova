from django_flatpickr.schemas import FlatpickrOptions
from django_flatpickr.widgets import DatePickerInput
from django.forms import ModelForm, DateField

from core.models import Bill, Payment


class BillForm(ModelForm):
    date_due = DateField(widget=DatePickerInput(options=FlatpickrOptions(altFormat="d/M/Y")))

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
        # widgets = {
        #     "fixed_cost": CheckboxInput(attrs={"id": "is-fixed"})
        # }

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
