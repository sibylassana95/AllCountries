from django.shortcuts import render
import requests
from django.core.cache import cache
from django.views.generic import TemplateView

def get_data():
    url = 'https://raw.githubusercontent.com/sibylassana95/AllCountries/main/countries.json'
    data = cache.get(url)
    if not data:
        response = requests.get(url)
        data = response.json()
        cache.set(url, data)
    return data


def index(request):
    pays = get_data()
    query = request.GET.get('q')
    if query:
        pays = [pay for pay in pays if query.lower() in pay['name'].lower()]
    context = {'pays': pays, 'query': query}
    return render(request, 'index.html', context)

from django.shortcuts import render
from .forms import UserProfileForm

from django.views.generic import TemplateView

def contact(request):
    form = UserProfileForm()
    return render(request, 'contact.html', {'form': form})

