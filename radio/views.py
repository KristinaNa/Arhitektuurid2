from django.shortcuts import render
from radio.models import Radio


def radio_list(request):
    data = Radio.objects.all().values()
    return render(request, 'view_radio_list.html', {'data': data})

def change_radio(request):
    return render(request, 'edit_radio.html')
