from django.http import HttpResponse
from django.shortcuts import render


def first_page(request):
    text = 'Hello world'
    number = 123
    return render(request, './index.html',{

        'text': text,
        'number': number


    })
