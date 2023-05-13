from django.contrib.auth.models import AbstractUser
from django.db import models


import json


# Ouvrir le fichier JSON
with open('countries.json', 'r') as f:
    countries = json.load(f)

# Extraire les codes de numérotation téléphonique de chaque pays
dial_codes = [country['dial_code'] for country in countries]

# Créer une liste de choix pour les codes de numérotation téléphonique
DIAL_CODES_CHOICES = [(code, code) for code in dial_codes]

class Utulisateur(AbstractUser):
    phone_number_code = models.CharField(max_length=8, choices=DIAL_CODES_CHOICES)
    phone_number = models.CharField(max_length=15)
    

    def get_phone_number(self):
        return '{} {}'.format(self.phone_number_code, self.phone_number)
