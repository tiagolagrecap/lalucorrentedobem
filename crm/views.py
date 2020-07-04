from django.shortcuts import render, redirect, reverse
from .models import *
from .forms import CustomerForm
from .filters import CustomerFilter
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.forms import inlineformset_factory







def home(request):
    customers = Customer.objects.all()

    total_customers = customers.count()

    concluido = customers.filter(status='Concluido').count()
    pendente = customers.filter(status='Pendente').count()

    myFilter = CustomerFilter(request.GET, queryset=customers)
    customers = myFilter.qs

    context = {'customers': customers, 'total_customers': total_customers, 'concluido': concluido, 'pendente': pendente
        , 'myFilter': myFilter}
    return render(request, 'crm/dashboard.html', context)


@staff_member_required
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    context = {'customer': customer}
    return render(request, 'crm/customer.html', context)



@staff_member_required
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'crm/customer_form.html', context)


@staff_member_required
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('/')

    context = {'item': customer}
    return render(request, 'crm/delete.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')

@staff_member_required
def createCustomer(request):

    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'crm/customer_form.html', context)
