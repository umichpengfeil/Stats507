# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
#
# + [Dropping](#Dropping) 

# ## Dropping
#
# __Pengfei Liu__    
# 2021/11/16

# ## Dropping In Pandas
# - Delete (some parts of) data samples under certain conditions using `pd.drop()`.
# - Use `axis` to choose to drop from the index(`0` or `index`) or columns(`1` or `columns`).
# - General usage: `df.drop(df[<some boolean condition>].index)`

import numpy as np
import pandas as pd
df1 = pd.DataFrame(np.arange(24).reshape(6, 4), columns=['A', 'B', 'C', 'D'])
print(df1)
#drop columns
print(df1.drop(['B','C'], axis = 1))
#drop the items that is less than 6 in column A.
print(df1.drop(df1[df1['A'] < 6].index))

# - In the previous test, we showed the importance of `labels`, which was `df1[df1['A'] < 6].index` there.
# - we can also use the parameter `level` to make multiple indexing.
#

midx = pd.MultiIndex(levels=[['lama', 'cow', 'falcon'],
                             ['speed', 'weight', 'length']],
                     codes=[[0, 0, 0, 1, 1, 1, 2, 2, 2],
                            [0, 1, 2, 0, 1, 2, 0, 1, 2]])
df = pd.DataFrame(index=midx, columns=['big', 'small'],
                  data=[[45, 30], [200, 100], [1.5, 1], [30, 20],
                        [250, 150], [1.5, 0.8], [320, 250],
                        [1, 0.8], [0.3, 0.2]])
print(df)
print(df.drop(index = 'cow', columns = 'small'))

# - We also have other relative functions such as `pd.dropna()` and `pd.drop_duplicates()`.
