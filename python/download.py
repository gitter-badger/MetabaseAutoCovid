#!/usr/bin/env python3
import requests
from common import files

downloadBase = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"

for item in files:
    url = downloadBase + item["sourceName"]
    print("Getting ", url)
    r = requests.get(url)

    # Retrieve HTTP meta-data
    if r.status_code != 200:
        raise "Didn't get status code 200"

    with open(item["downloadName"], 'wb') as f:
        f.write(r.content)