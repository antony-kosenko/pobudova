from django.contrib.auth.decorators import login_required
from django.db.models import F, Min, Max
from django.shortcuts import render
from django.views.generic import ListView

import re

from core.forms import BillForm, PaymentForm
from core.models import Payment, Bill
from .filters import BillFilter


def starting_view(request):
    """ Renders a starting page (introduction page) a User sees once entered on the app page """
    return render(request, 'core/starting_page.html')


@login_required()
def home_view(request):
    return render(request, "core/home.html")


@login_required()
def last_bills_view(request):
    """ Renders a list of two rows: for receipts still pending a payment and receipts recently paid out.
    Ordered by record date (not a due date)."""
    current_user = request.user

    last_pending_bills = Payment.objects.filter(user=current_user, is_closed=False).order_by('record_date')\
                                       .annotate(service_name=F('bill__service_name'), date_due=F('bill__date_due'))[:4]
    last_closed_bills = Payment.objects.filter(user=current_user, is_closed=True).order_by('record_date')\
                                       .annotate(service_name=F('bill__service_name'), date_due=F('bill__date_due'))[:4]

    context = {
        'last_pending_bills': last_pending_bills,
        'last_closed_bills': last_closed_bills
    }

    return render(request, "core/hub_last_bills.html", context)


@login_required()
def create_record_view(request):
    """ Renders a Bill model form to create a new receipt record.
    Additionally, renders an 'actual payment' field from Payment form for tracking receipt's status (closed/pending)"""

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
                # TODO Integrate a consumption record
                is_closed = True
            else:
                is_closed = False

            Payment.objects.create(bill=new_bill_object,
                                   user=user,
                                   expected_payment=new_bill_object.cost_due,
                                   actual_payment=new_payment_form.cleaned_data['actual_payment'],
                                   is_closed=is_closed)
        else:
            #  TODO Remove an error print once all validations and indication within a form completed
            print(new_bill_form.errors.as_data())
    context = {
        "bill_form": bill_form,
        "payment_form": payment_form
    }
    return render(request, "core/hub_new_service_record.html", context)


class BillsListView(ListView):
    model = Bill
    paginate_by = 10
    template_name = 'core/hub_bills_list.html'
    ordering = ['-date_due']
    filterset_class = BillFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year_list = Bill.objects.filter(payment__user=self.request.user).order_by('-date_due__year').values_list(
            'date_due__year', flat=True).distinct()
        service_list = Bill.objects.filter(payment__user=self.request.user).order_by('service_name').values_list(
            'service_name', flat=True).distinct()
        context['years'] = year_list
        context['services'] = service_list
        context['filter'] = self.filterset_class(self.request, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        year = self.request.GET.get('year')
        month = self.request.GET.get('month')
        service_name = self.request.GET.get('service_name')

        if year:
            queryset = queryset.filter(date_due__year=year)

        if month:
            queryset = queryset.filter(date_due__month=month)

        if service_name:
            queryset = queryset.filter(service_name=service_name)

        return queryset
