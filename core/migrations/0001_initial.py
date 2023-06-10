# Generated by Django 4.1.7 on 2023-06-10 16:55

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=30, verbose_name='Service name')),
                ('date_due', models.DateField(verbose_name='Date related for payment')),
                ('date_registered', models.DateField(auto_now_add=True, verbose_name='Date of bill registered')),
                ('date_updated', models.DateField(auto_now=True, verbose_name='Date of bill data updated')),
                ('is_fixed_cost', models.BooleanField(default=False, verbose_name='Is bill a fixed cost')),
                ('unit', models.CharField(blank=True, default=None, max_length=5, null=True, verbose_name='Unit')),
                ('current_counter', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('consumption', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('cost_due', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('is_paid', models.BooleanField(default=False, verbose_name='Completely paid')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_date', models.DateField(auto_now_add=True)),
                ('expected_payment', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('actual_payment', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('bill', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='core.bill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
