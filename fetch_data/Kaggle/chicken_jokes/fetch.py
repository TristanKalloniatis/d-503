# ---
# jupyter:
#   jupytext_format_version: '1.3'
#   jupytext_formats: py:light
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.6
# ---

# # fetch Kaggle short joke data and extract chicken jokes

import pandas as pd
import string
import re

### Read Kaggle's raw short joke data and change the max number of characters to print to screen.
rawjokes = pd.read_csv("../../../Data/Kaggle/shortjokes.csv", index_col=0) 
pd.options.display.max_colwidth = 500

rawchickenjokes = rawjokes.loc[rawjokes.Joke.str.contains('why did the chicken', case=False),:].reset_index()
rawchickenjokes.to_csv("../../../Data/Kaggle/shortjokes_chicken_raw.csv", columns=['ID','Joke'])
shortjokes_chicken_clean = pd.read_csv("../../../Data/Kaggle/shortjokes_chicken_clean.csv", index_col=0) 
shortjokes_chicken_clean

# This data is messy (it contains many grammatical mistakes and also includes some controversial humour). Consequently, this data has been manually cleaned, and reformatted to shortjokes_chicken_clean.csv.

rawknockjokes = rawjokes.loc[rawjokes.Joke.str.contains('knock knock', case=False),:].reset_index()
rawknockjokes.to_csv("../../../Data/Kaggle/shortjokes_knock_raw.csv", columns=['ID','Joke'])
shortjokes_knock_clean = pd.read_csv("../../../Data/Kaggle/shortjokes_knock_clean.csv", index_col=0)
shortjokes_knock_clean
