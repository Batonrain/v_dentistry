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
        name = request.POST.get('name')
        howToConnect = request.POST.get('howToConnect')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = f'Желаемый способ связи: {howToConnect} \n\n Желаемое время записи: {date} в {time}'

        send_mail(
            f'Новая запись на приём от {name}',
            message,
            'drzatulkin@yandex.ru',
            ['drzatulkin@yandex.ru'],  # Замените настройками своего адреса электронной почты получателя
            fail_silently=False,
        )

        return render(request, 'appointment.html', {'success': True})

    return render(request, "appointment.html")


    