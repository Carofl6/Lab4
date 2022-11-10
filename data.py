
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: CAROFL6                                                                     -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import ccxt
import pandas as pd
import time
import datetime as dt

def raw_data_from_ccxt(cripto: str, timeframe : str, hours : int):
    
    results = {exchange : {} for exchange in ["bitso", "ftx", "kraken"]}
    bitso = ccxt.bitso() 
    ftx = ccxt.ftx()
    kraken = ccxt.kraken()
    
    i = 0
    while i < hours * 60: # hours * 60
        try:
            date = pd.to_datetime(dt.datetime.now())
        
            ob_bitso = bitso.fetch_order_book(cripto) 
            ohlcv_bitso = bitso.fetch_ohlcv(cripto, timeframe = timeframe, limit = 1)
        
            ob_ftx = ftx.fetch_order_book(cripto) 
            ohlcv_ftx = ftx.fetch_ohlcv(cripto, timeframe = timeframe, limit = 1)
        
            ob_kraken = kraken.fetch_order_book(cripto) 
            ohlcv_kraken = kraken.fetch_ohlcv(cripto, timeframe = timeframe, limit = 1)
        
            results["bitso"][date] = {}
            results["bitso"][date]["ob"] = ob_bitso
            results["bitso"][date]["ohlcv"] = ohlcv_bitso
        
            results["ftx"][date] = {}
            results["ftx"][date]["ob"] = ob_ftx
            results["ftx"][date]["ohlcv"] = ohlcv_ftx
        
            results["kraken"][date] = {}
            results["kraken"][date]["ob"] = ob_kraken
            results["kraken"][date]["ohlcv"] = ohlcv_kraken
            
            i += 1
            
        except:
            pass
        
        time.sleep(60)
        
    return results
