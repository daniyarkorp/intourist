from django.shortcuts import render
from .models import Place


# нам нужно получить весь список мест и отобразить
def places(request):
    place_objects = Place.objects.all() # отправляем запросы в базу данных SELECT *from
    return render(request, 'places.html', {'places':place_objects})