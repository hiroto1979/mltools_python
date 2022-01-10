#!/usr/bin/env python3

import pandas as pd
import numpy as np

def df_missing(df, cols):
    results = pd.DataFrame(columns=["name", "count", "missing", "percent"])
    for col in cols:
        total = len(df[col])
        missing = df[col].isnull().sum()
        percent = round(missing / total * 100, 2)
        result = pd.DataFrame([[col, total, missing, percent]], columns=["name", "count", "missing", "percent"])
        results = pd.concat([results, result])

    return results.reset_index(drop=True)


def df_dtypes(df, cols):
    t = df.dtypes
    results = pd.DataFrame(columns=["name", "dtype"])
    for i, v in t.items():
        result = pd.DataFrame([[i, v]], columns=["name", "dtype"])
        results = pd.concat([results, result])

    return results.reset_index(drop=True)


def df_summary(df, cols):
    missing = df_missing(df, cols)
    dt = df_dtypes(df, cols)
    results = pd.merge(missings, dt)

    return results.reset_index(drop=True)


def df_status(df):
    results = pd.DataFrame(columns=["name", "result"])
    result = pd.DataFrame([["rows", df.shape[0]]], columns=["name", "result"])
    results = pd.concat([results, result])
    result = pd.DataFrame([["columns", df.shape[1]]], columns=["name", "result"])
    results = pd.concat([results, result])

    return results.reset_index(drop=True)