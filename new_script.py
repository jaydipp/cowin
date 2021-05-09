import requests
import json
import pandas as pd
from state_district import get_all_districts

headers = {
    'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36"
}

def get_by_pin(pincode, date):
    response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}'
                            .format(pincode, date),
                            headers = headers)
    
    pincode = pd.DataFrame(json.loads(response.text)['centers'])
    sessions_df = pd.DataFrame()
    new_pincode = pd.DataFrame()
    for i in range(pincode.shape[0]):
        df = pd.DataFrame(pincode.loc[i].sessions)
        for j in range(df.shape[0]):
            new_pincode = new_pincode.append(pincode.loc[i], ignore_index = True)   
        sessions_df = sessions_df.append(df, ignore_index=True)
        final_df = pd.concat([new_pincode, sessions_df], axis = 1)
        
        
    return final_df

def get_by_district(district_name, date):
    districts = get_all_districts()
    response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={0}&date={1}"
                            .format(
            districts[district_name], date
        ),
        headers=headers)
    pincode = pd.DataFrame(json.loads(response.text)['centers'])
    sessions_df = pd.DataFrame()
    new_pincode = pd.DataFrame()
    for i in range(pincode.shape[0]):
        df = pd.DataFrame(pincode.loc[i].sessions)
        for j in range(df.shape[0]):
            new_pincode = new_pincode.append(pincode.loc[i], ignore_index = True)   
        sessions_df = sessions_df.append(df, ignore_index=True)
        final_df = pd.concat([new_pincode, sessions_df], axis = 1)
        
        
    return final_df
    
    

if __name__ ==  '__main__':
    date = '10-05-2021'
    pincode = 382424
    district_name = 'Bharuch'
    
print(get_by_district(district_name, date))
