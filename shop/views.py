from django.shortcuts import render
from . models import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView
# Create your views here.
def home(request):
	sales = Sale.objects.all().count()
	stock = Stock.objects.all().count()
	sales_today = Sale.objects.filter(date_sold=timezone.now().date().today()).count()

	context = {
		"sales": sales,
		"stock": stock,
		"sales_today": sales_today
	}

	return render(request, "index.html", context)


class StockList(ListView):
	model = Stock
	template_name = "stock.html"

class AddStock(CreateView):
	model = Stock
	fields = "__all__"
	template_name = "add-stock.html"

class SalesList(ListView):
	model = Sale
	template_name = "sales.html"

class AddSale(CreateView):
	model = Sale
	fields = "__all__"
	template_name = "add-sale.html"

class EmployeeList(ListView):
	model = Employee
	template_name = "employees.html"

class AddEmployee(CreateView):
	model = Employee
	fields = "__all__"
	template_name = "new-employee.html"


from django.shortcuts import render, redirect

from django.contrib.auth.models import User, auth
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'invalid creditials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("login")
