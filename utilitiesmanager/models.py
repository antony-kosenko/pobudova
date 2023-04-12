# from django.db import models
#
# from accounts.models import User
# # Create your models here.
#
#
# class Bill(models.Model):
#     service_name = models.CharField(max_length=30)
#     fixed_cost = models.BooleanField(default=False)
#     unit = models.CharField(max_length=5, null=True, blank=True)
#     current_counter = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
#     consumption = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
#     cost_per_unit = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
#     payed_amount = models.DecimalField(max_digits=8, decimal_places=2)
#     is_paid = models.BooleanField(default=False)
#
#
# class Payment(models.Model):
#     bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     record_date = models.DateTimeField(auto_now_add=True)
#     service_name = models.CharField(max_length=30)
#     year_due = models.IntegerField()
#     month_due = models.IntegerField()
#     payed_amount = models.DecimalField(max_digits=8, decimal_places=2)
