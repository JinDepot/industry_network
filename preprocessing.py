# This file loads and preprocesses the business description sections, saving the resulting table as a csv file
# Author: Hye Jin Lee
# Last Updated: 03-08-2023

import pandas as pd
import glob
import re

def main():
    # load data
    print('Loading data...')
    data_path = '/home/hyejin/data/'
    filelist = glob.glob(f'{data_path}/10-K/*', recursive=True)

    df = pd.DataFrame()

    for i, f in enumerate(filelist):
        print("   working on %s-th document..." %i, end='\r')
        # get ticker from filepath
        ticker = f.split('/')[-1].split('_')[0]

        with open(f, 'r') as content:
            content = content.read().replace('\r\n',' ').replace('\n',' ')
            content = re.sub(r'^\W*','',content)
            content = content.replace('Table of Contents',' ').replace('Overview', '').replace('OVERVIEW', '').replace('and Description of Major Subsidiaries ','')
            content = re.sub(r'^G(?:\s*eneral\s*)\b\s+','',content)
            content = ' '.join(content.split())
            content = content.strip()

        df.loc[i,'ticker'] = ticker
        df.loc[i,'content'] = content

    # add firm info
    print('Merging company information...')
    infos = pd.read_csv(f'{data_path}/sp500_namelist_2021.csv')
    sp500 = pd.merge(df, infos, left_on='ticker', right_on='Ticker', how='inner')

    # dump the resulting data
    sp500[['ticker','content','Rank','Company','Industry','Market Cap']].to_csv(f'{data_path}/sp500_all.csv', index=False)
    print('Done!')

if __name__ == '__main__':
    main()
