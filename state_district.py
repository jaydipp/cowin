import pandas as pd
import requests
import json
import itertools

headers = {
    'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36"
}

def get_states():
    response = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/states', headers=headers)
    states = pd.DataFrame(json.loads(response.text)['states'])
    states.set_index('state_name', inplace=True)
    state_dict = states.to_dict()['state_id']
    
    return state_dict


def get_all_districts():
    districts_df = pd.DataFrame()
    districts_dict = {}
    for i in range(1,37):
        response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(i), headers = headers)
        text = json.loads(response.text)['districts']
        df = pd.DataFrame(text)
        districts_df = districts_df.append(df, ignore_index=True)
        for i in range(districts_df.shape[0]):
            districts_dict[districts_df['district_name'][i]] = districts_df['district_id'][i]
            
    return districts_dict

def get_district(state_name):
    state_dict  = get_states()
    response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_dict[state_name]), headers = headers)
    text = json.loads(response.text)['districts']
    df = pd.DataFrame(text)
    
    return df

print(get_all_districts())
