from django.db import models

from accounts.models import User
# Create your models here.

# TODO Check validators (for negative values)


class Bill(models.Model):
    service_name = models.CharField(max_length=30)  # TODO Make a list of valid services. Not allowed to type in custom
    date_due = models.DateField()
    fixed_cost = models.BooleanField(default=False)
    unit = models.CharField(max_length=5, null=True, blank=True)  # TODO Make a list of valid units. Might be typed in custom?

    current_counter = models.DecimalField(max_digits=15,
                                          decimal_places=2,
                                          null=True,
                                          blank=True,
                                          )

    consumption = models.DecimalField(max_digits=8,   # TODO Check if possible to get previos record info and calculate a result
                                      decimal_places=2,
                                      null=True,
                                      blank=True)

    cost_per_unit = models.DecimalField(max_digits=6,
                                        decimal_places=2,
                                        null=True,
                                        blank=True,
                                        )

    cost_due = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Bill_{self.id}, {self.service_name}, {self.date_due}"


class Payment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    record_date = models.DateField(auto_now_add=True)
    expected_payment = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    actual_payment = models.DecimalField(max_digits=8,
                                         decimal_places=2,
                                         default=0.00,
                                         null=True,
                                         blank=True,
                                         )

    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment. User: {self.user_id}, Date: {self.record_date}"
