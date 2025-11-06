# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
input_data = dataiku.Dataset("input_dataset")
input_data_df = input_data.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
columns_type = "string"
row_cnt = 0

if columns_type == "string":
    output_data = input_data_df.select_dtypes(include=['object', 'string'])

elif columns_type != "string":
    output_data = input_data_df.select_dtypes(exclude=['object', 'string'])
    
else:
    output_data = output_data.copy()
    
if row_cnt != 0:
    output_data = output_data.iloc[:row_cnt, :]
else:
    pass

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
output_data_df = dataiku.Dataset("output_dataset")
output_data_df.write_with_schema(output_data)
