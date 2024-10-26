from django.shortcuts import render
import serial

def index(request):
    data = {
        'title': 'Домашняя страница кека',
        'values': ['Some', 'Body', 'Once',  'Told', 'Me']
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def data(request):
    header = "Данные"

    port = "COM4"
    baud = 9600
    s = serial.Serial(port, baudrate=baud)

    # Ожидание данных и сбор их пачкой
    data = {}
    while len(data) < 3:
        res = s.readline().decode().strip()

        if "Освещенность =" in res:
            data['light'] = res
        elif "Влажность:" in res:
            data['humidity'] = res
        elif "Температура :" in res:
            data['temperature'] = res

    # Передача данных в шаблон
    return render(request, 'main/data.html', {'header': header, 'data': data})