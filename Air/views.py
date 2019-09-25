from django.shortcuts import render
import os

# Create your views here.
def tests(request):
    return render(request, 'charts.html')


def forms(request):

    return render(request,'forms.html')

from Nike import settings
def upload(request):
    if request.method =='POST':
        f = request.FILES['file']
        fname = os.path.join(settings.MEDIA_ROOT,f.name)
        with open(r'{}'.format(fname), 'wb') as f1:
            for c in f.chunks():
                f1.write(c)
        print("picture OK", fname)
        post_pic =os.path.basename(fname)
        print(post_pic)
    return render(request,'upload.html')

def maps(request):
    return render(request,'maps.html')