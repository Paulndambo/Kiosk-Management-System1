from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Kiosk(models.Model):
	title = models.CharField(max_length=200)
	owner = models.CharField(max_length=200)
	postal_code = models.CharField(max_length=200)
	town = models.CharField(max_length=200)
	country = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class Employee(models.Model):
	employee_number = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=200)
	email = models.EmailField()
	postal_code = models.CharField(max_length=200)
	town = models.CharField(max_length=200)
	country = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("employees")

	def get_address(self):
		return self.postal_code + " - " +self.town + " - "+self.country


class Stock(models.Model):
	item = models.CharField(max_length=200)
	quantity = models.FloatField(default=0)
	price = models.FloatField(default=0)
	item_unit = models.CharField(max_length=20, default="Kg")
	date_recorded = models.DateField(default=timezone.now)

	def __str__(self):
		return self.item

	def get_cost_price(self):
		return self.quantity * self.price

	def get_absolute_url(self):
		return reverse("stock")

class Sale(models.Model):
	item = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)
	quantity = models.FloatField(default=0)
	sold_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
	item_unit = models.CharField(max_length=20, default="Kg")
	date_sold = models.DateField(default=timezone.now)

	def __str__(self):
		return str(self.item)

	def get_selling_price(self):
		return self.item.price * self.quantity

	def get_absolute_url(self):
		return reverse("sales")

