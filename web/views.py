from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def index_page(request):
    
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'phone':phone,
            'message':message,
        }
        message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Email:\n\t\t{}\n
        Phone:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['phone'])
        send_mail('You got a mail!', message, '', ['ch@gmail.com']) #  enter your email address
        
    return render(request, 'web/index.html', {})


    # if request.method == 'POST':
        
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     subject = request.POST.get('subject')
    #     message = request.POST.get('message')
    #     send_mail(subject, message, email, ['charlesuwagboe1984@gmail.com'], fail_silently=False)
        
    #     form_data = {name:'name', email:"email", subject:'subject', message:'message'}
        
        
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

    