# -*- coding: utf-8 -*-
import dataiku
import pandas as pd
from dataiku.customrecipe import get_input_names_for_role, get_output_names_for_role, get_recipe_config

# --- 1) input/output 데이터셋 읽기 ---
in_name = get_input_names_for_role("input_dataset")[0]
out_name = get_output_names_for_role("output_dataset")[0]

in_ds = dataiku.Dataset(in_name)
out_ds = dataiku.Dataset(out_name)



# --- 2) 파라미터 읽기 ---
config = get_recipe_config()
select_type = config.get("select_type", "string")  # "string" 또는 "numeric"
row_cnt = config.get("row_cnt", 0)


# --- 3) 입력 데이터 로드 ---
df = in_ds.get_dataframe()



# --- 4) 파이썬 코드(컬럼 선택 로직) ---
if select_type == "string":
    out_df = df.select_dtypes(include=["object", "string"])
    
elif select_type == "numeric":
    out_df = df.select_dtypes(include=["number"])
else:
    out_df = df.copy()

    
if row_cnt != 0:
    out_df = out_df.iloc[:row_cnt, :]
else:
    pass

# --- 5) 결과 쓰기 ---
out_ds.write_with_schema(out_df)
