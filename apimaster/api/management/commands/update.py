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
            try:
                x = str(data)
                print(x)
                r = requests.get('https://min-api.cryptocompare.com/data/price?fsym='+ x +'&tsyms=BTC&e=CCCAGG')
                json_data = r.json()
                # print(json_data)
                y = "%.8f" % float(str(json_data['BTC']))
                print(y)
                teste = Coinlist.objects.get(nick=x)
                teste.price = float(str(json_data['BTC']))
                new_worth = teste.ammount * teste.price
                teste.worth = new_worth
                print(teste.worth)
                teste.save()
            except:
                pass
