from pandas.core.frame import DataFrame
import requests
from requests.models import Response
import json
import pandas as pd

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://www.cowin.gov.in",
    "pragma": "no-cache",
    "referer": "https://www.cowin.gov.in/",
    "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
}


def calenderByPincode(pincode, date):
    response = requests.get(
        "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={0}&date={1}".format(
            pincode, date
        ),
        headers=headers,
    )

    return json.loads(response.text)["centers"]


def calenderByDistrict(district, date):

    # Hardcoded district ids of Gujarat
    # to get district id for any State, GET the following endpoint
    # https://cdn-api.co-vin.in/api/v2/admin/location/districts/11
    # Where 11 is the State ID of Gujarat
    # You can get state ID by selecting any State on coWIN portal and seeing the request id for it
    districts = {
        "Ahmedabad": "154",
        "Ahmedabad Corporation": "770",
        "Amreli": "174",
        "Anand": "179",
        "Aravalli": "158",
        "Banaskantha": "159",
        "Bharuch": "180",
        "Bhavnagar": "175",
        "Bhavnagar Corporation": "771",
        "Botad": "176",
        "Chhotaudepur": "181",
        "Dahod": "182",
        "Dang": "163",
        "Devbhumi Dwaraka": "168",
        "Gandhinagar": "153",
        "Gandhinagar Corporation": "772",
        "Gir Somnath": "177",
        "Jamnagar": "169",
        "Jamnagar Corporation": "773",
        "Junagadh": "178",
        "Junagadh Corporation": "774",
        "Kheda": "156",
        "Kutch": "170",
        "Mahisagar": "183",
        "Mehsana": "160",
        "Morbi": "171",
        "Narmada": "184",
        "Navsari": "164",
        "Panchmahal": "185",
        "Patan": "161",
        "Porbandar": "172",
        "Rajkot": "173",
        "Rajkot Corporation": "775",
        "Sabarkantha": "162",
        "Surat": "165",
        "Surat Corporation": "776",
        "Surendranagar": "157",
        "Tapi": "166",
        "Vadodara": "155",
        "Vadodara Corporation": "777",
        "Valsad": "167",
    }

    response = requests.get(
        "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={0}&date={1}".format(
            districts[district], date
        ),
        headers=headers,
    )

    return json.loads(response.text)["centers"]

def getSessionDetails(center_id: str, date: str, centers_df: DataFrame):

    centers_df.set_index("center_id", inplace=True)
    center = centers_df.loc[center_id]
    sessions = center.sessions
    session_df = pd.DataFrame(sessions)
    session_df.set_index("date", inplace=True)
    return session_df.loc[date]

if __name__ == "__main__":

    pincode = 392015
    date = "08-05-2021"
    centers = calenderByPincode(pincode, date)

    district = "Bharuch"
    centers = calenderByDistrict(district, date)

    centers_df = pd.DataFrame(centers)

    # Can select any center_id here (filter on available columns of centers_df)
    center_id = centers_df["center_id"][0]

    session_details = getSessionDetails(center_id, date, centers_df)

    print(session_details)
