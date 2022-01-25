import requests

def rari_price_check(contract, archetypes):
    '''
    Checks the price on Rarible.com to see if the price is within the set range
    Returns a Float or Int (based on request response)
    '''
    
    #create the headers to use for the item finder request, save as headers_items
    headers_items = {
        'authority': 'api-mainnet.rarible.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'sec-gpc': '1',
        'origin': 'https://rarible.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://rarible.com/',
        'accept-language': 'en-US,en;q=0.9',
    }
    
    #the data/payload for the items finder request, save as data_items
    data_items = '{"size":1,"filter":{"verifiedOnly":false,"sort":"LOW_PRICE_FIRST","collections":["TEZOS-' + contract + '"],"traits":[{"key":"Archetype","values":' + archetypes + '}],"currency":"TEZOS-tz1Ke2h7sDdakHJQh8WX4Z372du1KChsksyU","nsfw":true}}'
    
    #make the item finder request using headers_items and data_items, save the response as response_items
    response_items = requests.post('https://api-mainnet.rarible.com/marketplace/search/v1/items', headers=headers_items, data=data_items)
    
    #get the json response from response_items, save as response_items_json
    response_items_json = response_items.json()
    
    #get the item id for the located item and save as item_id
    item_id = response_items_json[0]["id"]
    
    #create the headers for the map request, save as headers_map
    headers_map = {
        'authority': 'api-mainnet.rarible.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'sec-gpc': '1',
        'origin': 'https://rarible.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://rarible.com/',
        'accept-language': 'en-US,en;q=0.9',
    }
    
    #create the data/payload for the map request, save as data_map
    data_map = f'["{item_id}"]'
    
    #make the map request using headers_map and data_map, save the response as response_map
    response_map = requests.post('https://api-mainnet.rarible.com/marketplace/api/v4/items/map', headers=headers_map, data=data_map)
    
    #get the json response from response_map, save as response_map_json
    response_map_json = response_map.json()
    
    #get the price from the json data, save as price
    price = response_map_json[0]["item"]["ownership"]["price"]
    
    #return price as the result of the function
    return price