from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.forms import BillForm, PaymentForm
from core.models import Payment


def starting_view(request):
    """ Renders a starting page(introduction page) a User sees once entered on the app page """
    return render(request, 'core/starting_page.html')


@login_required()
def home_view(request):
    return render(request, "core/home.html")


@login_required()
def hub_view(request):

    return render(request, "core/hub.html")


@login_required()
def create_record_view(request):
    bill_form = BillForm()
    payment_form = PaymentForm()
    if request.method == "POST":
        new_bill_form = BillForm(request.POST)
        new_payment_form = PaymentForm(request.POST)
        if new_bill_form.is_valid() and new_payment_form.is_valid():
            user = request.user
            new_bill_object = new_bill_form.save()
            if new_payment_form.cleaned_data['actual_payment'] == new_bill_object.cost_due:
                # TODO Create a separate form for actual payment with one value
                # TODO Add a today's date above date choose for convenience
                is_closed = True
            else:
                is_closed = False
            Payment.objects.create(bill=new_bill_object,
                                   user=user,
                                   expected_payment=new_bill_object.cost_due,
                                   actual_payment=new_payment_form.cleaned_data['actual_payment'],
                                   is_closed=is_closed)

    context = {
        "bill_form": bill_form,
        "payment_form": payment_form
    }
    return render(request, "core/new_service_record.html", context)


def get_last_bills_view(request):
    
    return render(request, "core/last_bills.html")
