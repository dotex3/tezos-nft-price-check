import requests

def objkt_price_check(contract, filter_id):
    '''
    Checks the price on Objkt.com to see if the price is within the set range
    Returns a Float
    '''
    
    #GET request payload
    payload = {"value.fa2":contract, "value.objkt_id.as":filter_id, "active":"true", "select":"value"}
    
    #GET request
    response = requests.get('https://api.tzkt.io/v1/contracts/KT1FvqJwEDWb1Gwc55Jd1jjTHRVWbYKUUpyq/bigmaps/asks/keys', params=payload)
    
    #Turn the response into a json variable
    response_json = response.json()
    
    #initialize the price variable
    price = None
    
    for objkt in response_json:
        
        if price == None:
            price = float(objkt['xtz_per_objkt']) / 1000000
        
        elif float(objkt['xtz_per_objkt']) <= price * 1000000:
            price = float(objkt['xtz_per_objkt']) / 1000000
            
        else:
            pass
        
    #return price as the result of the function
    return price