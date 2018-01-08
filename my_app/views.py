from django.shortcuts import render


def home(request):
    context = dict()
    options = ['exchange_calculator', 'my_account', 'tourist_info']
    context['options'] = options
    return render(request, 'home.html', context)
