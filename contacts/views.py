from django.shortcuts import render ,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email= request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,"You hava already maded an inquiry!")
                return redirect('/listings/'+listing_id)


        contact = Contact(phone=phone,listing_id=listing_id,listing=listing,name=name,email=email,message=message,user_id=user_id)
        contact.save()
        send_mail(
            'Property Listing Inquiry',
            'There ia an inquiry for '+ listing +'Sign into the admin panel for more',
            'knaomii1004@gmail.com',
            [realtor_email, 'knauman1004@gmail.com'],
            fail_silently=False

        )
        messages.success(request, "Your request has been Submitted, a realtor will get back to you soon!")
        return redirect('/listings/'+listing_id)

