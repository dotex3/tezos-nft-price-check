from rariblemarketapi import rari_price_check
from objktmarketapi import objkt_price_check
from configparser import ConfigParser
from sys import path as syspath
from os import path as ospath
from time import sleep
import requests

print('Starting up...')
print('Powered by TzKT API | https://www.TzKT.io')

try:
    config = ConfigParser()

    config.read(ospath.join(syspath[0], "settings.ini"))
    
except:
    print('An error occurred while parsing the settings file! Program has failed.')

while True:
    
    if config.getboolean('Rarible', 'enable_rari') == True:
        
        try:
            
            rari_price = rari_price_check(config.get('Global', 'contract_address'), config.get('Rarible', 'Archetypes'))
            
            print('Current Rarible Price: ', rari_price)
            
            if rari_price <= float(config.get('Global', 'max_price')):
                
                print("Price is within the range!")
                
                rari_ifttt_name = config.get('Rarible', 'rari_ifttt_name')
                
                ifttt_key = config.get('Global', 'ifttt_key')
                
                requests.get(f'https://maker.ifttt.com/trigger/{rari_ifttt_name}/with/key/{ifttt_key}')
            else:
                print('The Rarible price is too high.')
                
        except:
            print('An error occurred during Rarible price check, program will retry later!')
            
    else:
        pass

    if config.getboolean('Objkt', 'enable_objkt') == True:
    
        try:
            
            objkt_price = objkt_price_check(config.get('Global', 'contract_address'), config.get('Objkt', 'filter_id'))
            
            print('Current Objkt Price: ', objkt_price)
            
            if objkt_price <= float(config.get('Global', 'max_price')):
                
                print("Price is within the range!")
                
                objkt_ifttt_name = config.get('Objkt', 'objkt_ifttt_name')
                
                ifttt_key = config.get('Global', 'ifttt_key')
                
                requests.get(f'https://maker.ifttt.com/trigger/{objkt_ifttt_name}/with/key/{ifttt_key}')
            else:
                print('The Objkt price is too high.')
                
        except:
            print('An error occurred during Objkt price check, program will retry.')
            
    else:
        pass
        
    sleep(300)