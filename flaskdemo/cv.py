import datetime

import requests
import pandas as pd
from io import StringIO


states = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AS": "American Samoa",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "District Of Columbia",
    "FM": "Federated States Of Micronesia",
    "FL": "Florida",
    "GA": "Georgia",
    "GU": "Guam",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MH": "Marshall Islands",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "MP": "Northern Mariana Islands",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PW": "Palau",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VI": "Virgin Islands",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}


def epoch_to_time(value):
    timestamp = datetime.datetime.fromtimestamp(value).strftime('%m-%d-%Y %H:%M:%S')
    return timestamp


def get_timeseries(state_abbr):
    state_abbr = state_abbr.upper()
    state_name = states[state_abbr]
    api = 'http://coronavirusapi.com/getTimeSeries/{}'.format(state_abbr)
    with requests.get(api) as r:
        data = StringIO(r.text)
    df = pd.read_csv(data)
    df.fillna(0, inplace=True)
    df['deaths'] = df['deaths'].astype(int)
    df['seconds_since_Epoch'] = df['seconds_since_Epoch'].apply(epoch_to_time)
    return df.to_html(table_id='example', classes='display',
                      border=0, index=None), state_name
