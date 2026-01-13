from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Customer
from django.views.decorators.http import require_http_methods


@login_required
@require_http_methods(['GET'])
def customer_list(request):
    customers = Customer.objects.all()

    if request.headers.get('Content-Type') == 'aplication/json':
        customers_data = [
            {'name': customer.name,
             'vat_id': customer.vat_id,
             'street': customer.street,
             'city': customer.city,
             'country': customer.country
             }
            for customer in customers
        ]
    return JsonResponse(customers_data, safe=True)


@login_required
@require_http_methods(['POST'])
def customer_create(request):
    
