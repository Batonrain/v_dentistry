from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
  
def index(request):
    return render(request, "index.html")
 
def contacts(request):
    return render(request, "contacts.html")

def about(request):
    return render(request, "about.html")

def patients(request):
    return render(request, "about.html")

def doctors(request):
    return render(request, "doctors.html")

def cost(request):
    return render(request, "cost.html")

def appointment(request):
    if request.method == 'POST':
        print(request.POST)
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = f'Мобильный телефон пациента: {phone} \n\n Желаемое время записи: {date} в {time}'

        send_mail(
            f'Новая запись на приём от {firstName} {lastName}',
            message,
            'batonrain@yandex.ru',
            ['batonrain@yandex.ru'],  # Замените настройками своего адреса электронной почты получателя
            fail_silently=False,
        )

        return render(request, 'appointment.html', {'success': True})

    return render(request, "appointment.html")


    