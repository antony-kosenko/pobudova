from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from decimal import Decimal


# TODO Check validators (for negative values)

User = get_user_model()


class Bill(models.Model):

    """ Represents a Bill object which stores an information (such as counters, cost etc.)  """

    service_name = models.CharField(max_length=30, verbose_name="Service name")  # TODO Make a list of valid services. Might be typed in custom?
    date_due = models.DateField(verbose_name="Date related for payment")
    date_registered = models.DateField(auto_now_add=True, verbose_name="Date of bill registered")
    date_updated = models.DateField(auto_now=True, verbose_name="Date of bill data updated")
    is_fixed_cost = models.BooleanField(default=False, verbose_name="Is bill a fixed cost")
    unit = models.CharField(max_length=5, null=True, blank=True, default=None, verbose_name="Unit")  # TODO Make a list of valid units. Might be typed in custom?

    current_counter = models.DecimalField(max_digits=15,
                                          decimal_places=2,
                                          null=True,
                                          blank=True,
                                          validators=[MinValueValidator(Decimal('0.00'))]
                                          )

    consumption = models.DecimalField(max_digits=8,   # TODO Check if possible to get previos record info and calculate a result
                                      decimal_places=2,
                                      null=True,
                                      blank=True)

    cost_per_unit = models.DecimalField(max_digits=6,
                                        decimal_places=2,
                                        null=True,
                                        blank=True,
                                        validators=[MinValueValidator(Decimal('0.00'))]
                                        )

    cost_due = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    is_paid = models.BooleanField(default=False, verbose_name="Completely paid")

    def __str__(self):
        return f"Bill[{self.id}] | {self.service_name}, {self.date_due}, {self.cost_due}"


class Payment(models.Model):

    """ Represents a payment check. Stores an information such as user object who process a payments, cost value
     paid and date of payment."""

    bill = models.OneToOneField(Bill, on_delete=models.CASCADE, related_name="payments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    record_date = models.DateField(auto_now_add=True)
    expected_payment = models.DecimalField(max_digits=8,
                                           decimal_places=2,
                                           default=0.00,
                                           validators=[MinValueValidator(Decimal('0.00'))])

    actual_payment = models.DecimalField(max_digits=8,
                                         decimal_places=2,
                                         default=0.00,
                                         null=True,
                                         blank=True,
                                         validators=[MinValueValidator(Decimal('0.00'))]
                                         )

    def __str__(self):
        return f"PaymentID[{self.id}] | " \
               f"userID[{self.user_id}], " \
               f"date[{self.record_date}], " \
               f"cost[{self.expected_payment}]," \
               f"payed[{self.actual_payment}]"
