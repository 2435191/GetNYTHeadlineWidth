# run with ~/Library/LaunchAgents/nytHeadlines.plist

import pandas
import time, datetime
from get_nyt_data import get_headline

def push_data(fp='data.csv'):
    try:
        df = pandas.read_csv(fp, index_col='rawtime')
    except FileNotFoundError:
        df = pandas.DataFrame(columns=['rawtime', 'datetime', 'link', 'size', 'title'])
        df.set_index('rawtime', inplace=True)

    data = get_headline()

    if df.empty or not df.tail(1)[['link', 'size', 'title']].squeeze().equals(pandas.Series(data)): # only append to csv file if one of link, size, or title is different
        rawtime = time.time()
        datetime_ = datetime.datetime.fromtimestamp(rawtime)

        data['datetime'] = datetime_
        
        df.loc[rawtime] = data   
        df.to_csv(fp)

if __name__ == '__main__':
    push_data()
