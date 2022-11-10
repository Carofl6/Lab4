
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: Carofl6                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

from plotly.subplots import make_subplots
import plotly.graph_objects as go

def microstructure_visual(data, results, symbol):
    fig = make_subplots(rows = 3, cols = 2, subplot_titles = tuple(data.columns), x_title = "Date")
    cols = list(data.columns)
    
    for exchange in results.keys():
        fig.add_trace(go.Scatter(x = data.loc[exchange].index, y = data.loc[exchange][cols[0]], name = exchange),
                      row = 1, col = 1)
        
        fig.add_trace(go.Scatter(x = data.loc[exchange].index, y = data.loc[exchange][cols[1]], name = exchange),
                      row = 1, col = 2)
        
        fig.add_trace(go.Scatter(x = data.loc[exchange].index, y = data.loc[exchange][cols[2]], name = exchange),
                      row = 2, col = 1)
        
        fig.add_trace(go.Scatter(x = data.loc[exchange].index, y = data.loc[exchange][cols[3]], name = exchange),
                      row = 2, col = 2)
        
        fig.add_trace(go.Scatter(x = data.loc[exchange].index, y = data.loc[exchange][cols[4]], name = exchange),
                      row = 3, col = 1)
        
        fig.add_trace(go.Scatter(x = data.loc[exchange].index, y = data.loc[exchange][cols[5]], name = exchange),
                      row = 3, col = 2)
        
    fig.update_yaxes(title_text = "Levels", row = 1, col = 1)
    fig.update_yaxes(title_text = "Volume", row = 1, col = 2)
    fig.update_yaxes(title_text = "Volume", row = 2, col = 1)
    fig.update_yaxes(title_text = "Volume", row = 2, col = 2)
    fig.update_yaxes(title_text = "USD", row = 3, col = 1)
    fig.update_yaxes(title_text = "USD", row = 3, col = 2)
    
    fig.update_layout(showlegend = False, title_text = "Market Microstructure Visual: " + symbol, height = 750, width = 900)
    
    return fig
