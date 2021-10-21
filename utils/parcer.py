import requests
import re
from io import StringIO
import time
import pandas as p

HEADERS = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36',
            'accept': '*/*'}


def get_link(title):
    rew = requests.get(
        'https://finance.yahoo.com/quote/' + title + '/history',
        headers=HEADERS
    )
    crumb = None
    pattern = re.compile('.*"CrumbStore":{"crumb":"(?P<crumb>[^"]+)"}')
    for line in rew.text.splitlines():
        info = pattern.match(line)
        if info:
            crumb = info.groupdict()['crumb']
    date = int(time.time())
    dict = {'title': title, 'date': date,
                'crumb': crumb}
    get_csv = 'https://query1.finance.yahoo.com/v7/finance/download/' \
              '{title}?period1=0&period2={date}&interval=1d&events=history' \
              '&crumb={crumb}'.format(**dict)
    print(get_csv)
    response = requests.get(get_csv, headers=HEADERS)
    return p.read_csv(StringIO(response.text), parse_dates=['Date'])
