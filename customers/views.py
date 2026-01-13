from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Customer
from django.views.decorators.http import require_http_methods
from django import forms
from .forms import CustomerForm




@login_required
@require_http_methods(['GET'])
def customer_list(request):
    customers = Customer.objects.all()

    if request.headers.get('Accept') == 'application/json':
        customers_data = [
            {'name': customer.name,
             'vat_id': customer.vat_id,
             'street': customer.street,
             'city': customer.city,
             'country': customer.country
             }
            for customer in customers
        ]
        return JsonResponse(customers_data, safe=False)
    
    return render(request, 'customers/customer_list.html', {'customers': customers})


@login_required
@require_http_methods(['GET', 'POST'])
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    
    return render(request, 'customers/customer_create_form.html', {'form': form})
    

@login_required
@require_http_methods(['GET', 'POST'])
def customer_edit(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
        
    return render(request, 'customers/customer_edit_form.html', {'form': form})
    

    

