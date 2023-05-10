from django.shortcuts import render
import requests


def get_data():
    url = 'https://raw.githubusercontent.com/sibylassana95/AllCountries/main/countries.json'
    response = requests.get(url)
    data = response.json()
    return data


def index(request):
    pays = get_data()
    query = request.GET.get('q')
    if query:
        pays = [pay for pay in pays if query.lower() in pay['name'].lower()]
    context = {'pays': pays, 'query': query}
    return render(request, 'index.html', context)
