from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def success(request):

    return render(request,'success.html')

def send_email(request):

    context = {
        'mymail' : settings.EMAIL_HOST_USER
    }
        
    if request.method == 'POST':
    
        subject = request.POST['subject']
        message = request.POST['message']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['mail']]
        
        send_mail(subject, message, email_from, recipient_list)

        return redirect('http://127.0.0.1:8000/success/')
    
    return render(request,'send_email.html',context)
    
