
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import data, visualizations, functions

def lab_1(cripto: str, timeframe : str, hours : int):
    
    results = data.raw_data_from_ccxt(cripto, timeframe, hours)
    datan = functions.data_cleaning(results)
    
    return results, datan

def lab_2(results : dict, symbol : str):
    
    dataVisual = functions.data_from_microstructure(results)
    fig = visualizations.microstructure_visual(dataVisual, results, symbol)
    
    return dataVisual, fig

def lab_3(datan):
    
    return functions.effective_spread(datan)