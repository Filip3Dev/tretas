import json
import os
import requests
import logging
from django.utils.text import slugify
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from api.models import Coinlist

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not os.path.exists(os.path.join(settings.BASE_DIR, 'logs/task_update.log')):
    os.makedirs(os.path.join(settings.BASE_DIR, 'logs/task_update.log'))

handler = logging.FileHandler(os.path.join(settings.BASE_DIR, 'logs/task_cine.log'))
handler.setLevel(logging.INFO)

# https://www.cryptopia.co.nz/api/GetMarket/ARC_BTC
# https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ltc
# https://novaexchange.com/remote/v2/market/info/BTC_XZC/
# https://yobit.net/api/3/ticker/ltc_btc
# https://c-cex.com/t/dash-btc.json

class Command(BaseCommand):
    help = 'Faz o update dos dados da moeda'

    def handle(self, *args, **options):
        logger.info('Task de update iniciada')
        self.get_update()
        logger.info('Task de update finalizada')

    def get_update(self):
        for data in Coinlist.objects.all():
            x = str(data)
            print(x)
            try:
                teste = Coinlist.objects.get(nick=x)
                exchange = teste.exchange
                if exchange == "1":
                    print("Bittrex")
                    r = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-'+ x.lower())
                    json_data = r.json()
                    price = json_data['result'][0]['Last']
                    print("%.8f" % price)
                    teste.price = float(price)
                    new_worth = teste.ammount * teste.price
                    teste.worth = new_worth
                    teste.save()
                elif exchange == "2":
                    print("Cryptopia")
                    r = requests.get('https://www.cryptopia.co.nz/api/GetMarket/'+ x.upper() +'_BTC')
                    json_data = r.json()
                    price = json_data['Data']['LastPrice']
                    print("%.8f" % price)
                    teste.price = float(price)
                    new_worth = teste.ammount * teste.price
                    teste.worth = new_worth
                    teste.save()
                elif exchange == "3":
                    print("Novaexchange")
                    r = requests.get('https://novaexchange.com/remote/v2/market/info/BTC_'+ x.upper())
                    json_data = r.json()
                    price = json_data['markets'][0]['last_price']
                    print(price)
                    teste.price = float(price)
                    new_worth = teste.ammount * teste.price
                    teste.worth = new_worth
                    teste.save()
                elif exchange == "4":
                    print("Yobit")
                else:
                    print("CCex")
                pass
                # r = requests.get('https://min-api.cryptocompare.com/data/price?fsym='+ x +'&tsyms=BTC&e=CCCAGG')
                # json_data = r.json()
                # print(json_data)
                # y = "%.8f" % float(str(json_data['BTC']))
                # print(y)
                # teste.price = float(str(json_data['BTC']))
                # new_worth = teste.ammount * teste.price
                # teste.worth = new_worth
                # teste.save()
            except:
                pass
