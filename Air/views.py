from django.shortcuts import render


# Create your views here.
def tests(request):
    return render(request, 'charts.html')


def forms(request):
    return render(request,'forms.html')