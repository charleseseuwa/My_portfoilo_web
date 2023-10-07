from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from decouple import config

def index_page(request):
    if request.method == "POST":
        message_name = request.POST['message-name']  # here message-name comes from contact.html file's input type name
        message_email = request.POST['message-email']
        message = request.POST['message']

        ### Send an Email Start ###
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            config(['EMAIL_HOST_USER',]), # To email
        )
        ### Send an Email End ###

        return render(request, 'web/index.html', {'message_name':message_name})

    else:
        return render(request, 'web/contact.html', {})
    
    
def contact_page(request):
    if request.method == "POST":
        message_name = request.POST['message-name']  # here message-name comes from contact.html file's input type name
        message_email = request.POST['message-email']
        message = request.POST['message']

        ### Send an Email Start ###
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['charlesuwagboe1984@gmail.com',], # To email
        )
        ### Send an Email End ###
        return redirect("success")
    return render(request, 'web/index.html', {'message_name':message_name})

    # else:
    #     return render(request, 'web/contact.html', {})

    
def successView(request):
    return HttpResponse("Success! Thank you for your message.",)
    
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     subject = request.POST.get('subject')
    #     message = request.POST.get('message')
    #     form_data = {
    #         'name':name,
    #         'email':email,
    #         'subject':subject,
    #         'message':message,
    #     }
    #     message = '''
    #     From:\n\t\t{}\n
    #     Message:\n\t\t{}\n
    #     Email:\n\t\t{}\n
    #     Phone:\n\t\t{}\n
    #     '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['subject'])
    #     send_mail('You got a mail!', message, '', ['charlesuwagboe1984@gmail.com']) #  enter your email address
        
    # return render(request, 'web/index.html', {})


    
   
    
    # if request.method == 'GET':
    #     return render(request, 'web/index.html')
    
    # elif request.method == 'POST':
        
    #     message_name = request.POST.get("name")
    #     message_email = request.POST.get("email")
    #     message_subject = request.POST.get("subject")
    #     message = request.POST.get("message")

        
    #     send_mail(
            
    #         message_name,
    #         message_subject,
    #         message,
    #         message_email,
    #         ['cha@gmail.com']
     
     
            

    #     )
       
    #     return HttpResponse("Your message has been sent")
   
# Create your views here.

    