
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import numpy as np
import pandas as pd

def data_cleaning(results : dict):
    
    data = {}
    
    for exchange in results.keys():
        
        data[exchange] = {}
        
        for timestamp in results[exchange].keys():
            
            data[exchange][timestamp] = {}
            data[exchange][timestamp]["Ask"] = results[exchange][timestamp]["ob"]["asks"][0][0]
            data[exchange][timestamp]["Bid"] = results[exchange][timestamp]["ob"]["bids"][0][0]
            data[exchange][timestamp]["Ask Volume"] = results[exchange][timestamp]["ob"]["asks"][0][1]
            data[exchange][timestamp]["Bid Volume"] = results[exchange][timestamp]["ob"]["bids"][0][1]
            data[exchange][timestamp]["Spread"] = data[exchange][timestamp]["Ask"] - data[exchange][timestamp]["Bid"]
            data[exchange][timestamp]["Close_Price"] = results[exchange][timestamp]["ohlcv"][0][4]
    
    return data

def data_from_microstructure(results : dict):
    
    info = []
    for exchange in results.keys():
        for timestamp in results[exchange].keys():
            level = len(results[exchange][timestamp]["ob"]["bids"])
            ask_volume = sum([volume_i[1] for volume_i in results[exchange][timestamp]["ob"]["asks"]])
            bid_volume = sum([volume_i[1] for volume_i in results[exchange][timestamp]["ob"]["bids"]])
            total_volume = ask_volume + bid_volume
            mid_price = (results[exchange][timestamp]["ob"]["asks"][0][0] + 
                         results[exchange][timestamp]["ob"]["bids"][0][0]) / 2
            x, y = np.array([i[1] for i in results[exchange][timestamp]["ob"]["asks"]]), np.array([i[0] for i in results[exchange][timestamp]["ob"]["asks"]])
            a, b = np.array([i[1] for i in results[exchange][timestamp]["ob"]["bids"]]), np.array([i[0] for i in results[exchange][timestamp]["ob"]["bids"]])
            vwap = (np.dot(x, y) + np.dot(a, b)) / total_volume
            dummy_list = [level, ask_volume, bid_volume, total_volume, mid_price, vwap]
            info.append(dummy_list)
    
    k = list(results.keys())
    idx = pd.MultiIndex.from_product([list(results.keys()), 
                                      list(results[k[0]].keys())], names = ["exchange", "timeStamp"])
    data = pd.DataFrame(info, index = idx, 
                        columns = ["level", "ask_volume", "bid_volume", "total_volume", "mid_price", "vwap"])
    
    return data

def effective_spread(data):
    
    rollSpreads = {}
    for exchange in data.keys():
        df = pd.DataFrame()
        
        for timestamp in data[exchange].keys():
            df.loc[timestamp, "Close"] = data[exchange][timestamp]["Close_Price"]
            df.loc[timestamp, "Spread"] = data[exchange][timestamp]["Spread"]
                        
        df["Delta"] = df["Close"].diff()
        df["Roll Spread"] = np.nan

        for i in range(len(df) + 1):
            if i > 10:
                X = np.stack((list(df.iloc[i - 10 : i - 5, 2].values), list(df.iloc[i - 5 : i, 2].values)), axis = 0)
                cov = np.cov(X)
                df.iloc[i - 1, 3] = 2 * (abs(cov[1, 0])) ** 0.5
                
        df.drop(["Delta"], axis = 1, inplace = True)
        rollSpreads[exchange] = df
        
    return rollSpreads
