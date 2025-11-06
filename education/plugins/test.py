# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
car_data_1_joined = dataiku.Dataset("car_data_1_joined")
car_data_1_joined_df = car_data_1_joined.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
columns_type = "string"

if columns_type == "string":
    py_code2_df = car_data_1_joined_df.select_dtypes(include=['object', 'string'])

elif columns_type != "string":
    py_code2_df = car_data_1_joined_df.select_dtypes(exclude=['object', 'string'])

else:
  py_code2_df = car_data_1_joined_df.copy()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
py_code2 = dataiku.Dataset("py_code2")
py_code2.write_with_schema(py_code2_df)
