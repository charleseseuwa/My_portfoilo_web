from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def index_page(request):
    
    
    if request.method == 'GET':
        return render(request, 'web/index.html')
    
    elif request.method == 'POST':
        
        message_name = request.POST.get("name")
        message_email = request.POST.get("email")
        message_subject = request.POST.get("subject")
        message = request.POST.get("message")

        
        send_mail(
            
            message_name,
            message,
            message_email,
            ['charlesuwagboe1984@gmail.com']
     
     
            

        )
       
        return HttpResponse("Your message has been sent")
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
    #     subject:\n\t\t{}\n
    #     '''.format(form_data['name'], form_data['email'],form_data['subject'],form_data['message'])
    #     print('You got a mail!', message, '', ['charlesuwagboe1984@gmail.com']) # TODO: enter your email address
        
    # return render(request, 'web/index.html', {})
   
# Create your views here.
