from django.urls import path
from . views import *
from . import views

urlpatterns = [
 	path('', views.home, name="home"),
    path("stock/", StockList.as_view(), name="stock"),
    path("add-stock/", AddStock.as_view(), name="add-stock"),
    path("sales/", SalesList.as_view(), name="sales"),
    path("record-sale/", AddSale.as_view(), name="record-sale"),
    path("employees/", EmployeeList.as_view(), name="employees"),
    path("add-employee/", AddEmployee.as_view(), name="add-employee"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("profit-loss/", LossProfit.as_view(), name="profit-loss"),
 ]