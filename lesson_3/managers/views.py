from django.shortcuts import render

# Create your views here.
def managers_view(request):
    return render(request, 'managers/managers.html')