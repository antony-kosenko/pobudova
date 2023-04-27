import django_filters
from django.db.models.functions import ExtractYear

from .models import Bill


class BillFilter(django_filters.FilterSet):
    # Months dropdown menu's content
    MONTH_CHOICES = [(1, 'January[1]'), (2, 'February[2]'), (3, 'March[3]'), (4, 'April[4]'), (5, 'May[5]'),
                     (6, 'June[6]'), (7, 'July[7]'), (8, 'August[8]'), (9, 'September[9]'), (10, 'October[10]'),
                     (11, 'November[11]'), (12, 'December[12]')]

    year = django_filters.ChoiceFilter('date_due',
                                       label='Year')

    month = django_filters.ChoiceFilter('date_due',
                                        label='Month',
                                        choices=MONTH_CHOICES)

    service_name = django_filters.ChoiceFilter('service_name', label='Service Name')

    class Meta:
        model = Bill
        fields = ['service_name', 'year', 'month']

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

        # Getting year available for a current user and month (as per records made) in DESCENDING order.
        year_choices = Bill.objects.annotate(year=ExtractYear('date_due'))\
                                   .order_by('-year')\
                                   .values_list('year', flat=True)\
                                   .distinct()

        service_name_choices = Bill.objects.filter(payment__user=request.user) \
                                           .values_list('service_name', flat=True) \
                                           .distinct()

        # Defining tuples to represents a Year and Service name for choose option.
        year_choices = [(year, str(year)) for year in year_choices]
        service_name_choices = [(name, name) for name in service_name_choices]

        # Adding tuples defined above to the filters.
        self.filters['year'].extra['choices'] = year_choices
        self.filters['service_name'].extra['choices'] = service_name_choices
