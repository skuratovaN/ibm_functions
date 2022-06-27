import sys
import requests
import json

def main(dict):
    currency = dict["currency"]
    response = requests.get("https://belarusbank.by/api/kursExchange")
    value = response.json()[0]['{}_out'.format(currency)]
    return { 'value': value }