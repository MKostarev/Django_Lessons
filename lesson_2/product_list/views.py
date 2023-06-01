from django.shortcuts import render

from product_list.models import Food


# Create your views here.
def list_product (request):
    return render(request, 'product_list/index.html')

def list_product(request):
    foods = Food.objects.all().order_by('-id')
    context = {'foods': foods}

    return render(request, 'product_list/index.html', context)