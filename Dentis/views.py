from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .form import AppointmentModelForm


def index(request):
    if request.method == "POST":
        your_name = request.POST['your_name']
        your_phone = request.POST['your_phone']
        your_email = request.POST['your_email']
        your_address = request.POST['your_address']
        your_time = request.POST['your_time']
        your_message = request.POST['your_message']

        appointment = 'phone number :' + your_phone + 'time :' + your_time + 'address :' + your_address + 'main message' + your_message

        send_mail(
            your_name,  # subject
            appointment,  # message
            your_email,  # from email
            ['ndipdesmond247@gmail.com', 'ndip2tweenty47@gmail.com'],  # to the riciever it can be more than 1
        )
        return redirect('home')
        # form = AppointmentModelForm(request.POST or None)
        # if form.is_valid():
        #     form.save()

    return render(request, 'index.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        email_from = settings.EMAIL_HOST_USER
        # message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name,  # subject
            message,  # message
            email_from, # message comming from reciever
            # message_email,  # from email
            ['ndipdesmond247@gmail.com',],  # to the riciever it can be more than 1
        )

        return render(request, 'contact.html', {'message_name': message_name})
    return render(request, 'contact.html', {})


# def last_email(request):
#     if request.method == "POST":
#         message_name = "User Email"
#         message_email = "user@gmail.com"
#         message = request.POST['last_email']
#
#         send_mail(
#             message_name,  # subject
#             message,  # message
#             message_email,  # from email
#             ['ndipdesmond247@gmail.com', 'ndip2tweenty47@gmail.com'],  # to the riciever it can be more than 1
#         )
#
#         return redirect('home')
#     return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def service(request):
    return render(request, 'service.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def blog_details(request):
    return render(request, 'blog-details.html', {})










