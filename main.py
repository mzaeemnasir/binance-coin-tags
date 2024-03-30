import requests, pandas as pd

def update_symbols_list():
    url = "https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-products?includeEtf=true"
    response = requests.get(url)
    df = pd.DataFrame(response.json().get('data'))
    df = df[df['s'].str.endswith("USDT")] # filtering Data

    # creating a new data frame that will contains symbols and tags only
    
    df = pd.DataFrame(df, columns=["s", "tags"]) 
    df = df.rename(columns={"s":"symbol"})
    df = df.set_index('symbol')
    df = df.sort_index()
    
    df.to_csv("symbolsTags.csv") # saving the file
    
    
update_symbols_list()