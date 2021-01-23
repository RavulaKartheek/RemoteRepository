from django.shortcuts import render
from .models import ContactData

def home_page(request):
    return render(request, 'instituteapp/home.html')

def contact_page(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        comment1 = request.POST.get('comment')

        data = ContactData(
            name=name1,
            email=email1,
            comment=comment1
        )
        data.save()
        return render(request, 'instituteapp/contact.html')
    else:
        return render(request,'instituteapp/contact.html')

def gallery_page(request):
    return render(request, 'instituteapp/gallery.html')
