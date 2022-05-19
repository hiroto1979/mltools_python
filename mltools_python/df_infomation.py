#!/usr/bin/env python3

import pandas as pd
import numpy as np

# 欠損値を抽出し、データフレームにて表示を行う
def df_missing(df, cols=[]):
    if len(cols) == 0:
        cols = df.columns

    results = pd.DataFrame(columns=["name", "count", "missing", "percent"])
    for col in cols:
        total = len(df[col])
        missing = df[col].isnull().sum()
        percent = round(missing / total * 100, 2)
        result = pd.DataFrame([[col, total, missing, percent]], columns=["name", "count", "missing", "percent"])
        results = pd.concat([results, result])

    return results.reset_index(drop=True)

# データ型を抽出し、データフレームにて表示を行う
def df_dtypes(df):
    t = df.dtypes
    results = pd.DataFrame(columns=["name", "dtype"])
    for i, v in t.items():
        result = pd.DataFrame([[i, v]], columns=["name", "dtype"])
        results = pd.concat([results, result])

    return results.reset_index(drop=True)


# 欠損値+データ型を抽出し、データフレームにて表示を行う（全件のみ）
def df_summary(df):
    missing = df_missing(df)
    dt = df_dtypes(df)
    results = pd.merge(missings, dt)

    return results.reset_index(drop=True)


def df_status(df):
    results = pd.DataFrame(columns=["name", "result"])
    result = pd.DataFrame([["rows", df.shape[0]]], columns=["name", "result"])
    results = pd.concat([results, result])
    result = pd.DataFrame([["columns", df.shape[1]]], columns=["name", "result"])
    results = pd.concat([results, result])

    return results.reset_index(drop=True)
