"""
team2_TrafficLabellingClean.py
-------------------------------
Functions:
- Safe CSV reader (utf-8-sig with latin1 fallback).
- Basic cleaning: dropna, duplicates, constant columns,
  IP/Timestamp columns, extreme values.
- Lightweight feature selection: low variance filter +
  high correlation filter.
- Numeric optimization: downcast + rounding to reduce file size.
- Outputs both cleaned CSV and validation report directly into /datasets.
"""

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold

# ---------------- Paths ----------------
# Source dataset folder (update this path if needed)
DATA_FOLDER = r"C:\Users\hi\AI-CloudSec-System\data\traffic"

# Output directory: /datasets inside the repo
SCRIPT_PATH = os.path.abspath(__file__)
PROJECT_DIR = os.path.dirname(SCRIPT_PATH)
OUT_DIR = os.path.join(PROJECT_DIR, "datasets")
os.makedirs(OUT_DIR, exist_ok=True)

OUT_FILE = os.path.join(OUT_DIR, "team2_TrafficLabellingClean.csv")
REPORT = os.path.join(OUT_DIR, "team2_TrafficLabellingClean_report.txt")


# ---------------- Safe CSV Reader ----------------
def safe_read_csv(path):
    try:
        print(f"Reading {path} with utf-8-sig ...")
        return pd.read_csv(path, low_memory=False, encoding="utf-8-sig")
    except UnicodeDecodeError:
        print(f"⚠️ UTF-8 failed for {path}, retrying with latin1 ...")
        return pd.read_csv(path, low_memory=False, encoding="latin1")


# ---------------- Cleaning ----------------
def clean_dataframe(df, log):
    before = len(df)
    df = df.dropna().drop_duplicates()
    log.append(
        f"Dropna + duplicates: {before - len(df)} rows removed, now {len(df)} rows"
    )

    const_cols = df.columns[df.nunique() <= 1].tolist()
    if const_cols:
        df = df.drop(columns=const_cols)
        log.append(f"Dropped {len(const_cols)} constant cols: {const_cols}")

    drop_cols = [c for c in df.columns if "IP" in c or "Timestamp" in c]
    if drop_cols:
        df = df.drop(columns=drop_cols, errors="ignore")
        log.append(f"Dropped {len(drop_cols)} IP/Timestamp cols")

    if " Flow Duration" in df.columns:
        df = df[(df[" Flow Duration"] > 0) & (df[" Flow Duration"] < 3600)]
    if " Flow Bytes/s" in df.columns:
        df = df[df[" Flow Bytes/s"] < 1e9]

    return df


# ---------------- Feature Selection ----------------
def feature_selection(df, log, label_col=" Label"):
    if label_col in df.columns:
        X = df.drop(columns=[label_col], errors="ignore")
    else:
        X = df

    X = X.select_dtypes(include=np.number)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    selector = VarianceThreshold(threshold=0.01)
    X_var = selector.fit_transform(X_scaled)
    kept_cols = X.columns[selector.get_support()]
    log.append(f"Low variance removed: {X.shape[1] - len(kept_cols)} cols")

    X_df = pd.DataFrame(X_var, columns=kept_cols)
    corr = X_df.corr().abs()
    upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    to_drop = [col for col in upper.columns if any(upper[col] > 0.95)]
    if to_drop:
        X_df = X_df.drop(columns=to_drop)
        log.append(f"High correlation removed: {len(to_drop)} cols")

    if label_col in df.columns:
        X_df[label_col] = df[label_col].values

    return X_df


# ---------------- Numeric Optimization ----------------
def optimize_numeric(df, log, decimals=2):
    before_mem = df.memory_usage(deep=True).sum() / (1024 * 1024)
    for col in df.select_dtypes(include=[np.number]).columns:
        if pd.api.types.is_integer_dtype(df[col]):
            df[col] = pd.to_numeric(df[col], downcast="integer")
        else:
            df[col] = df[col].round(decimals)
            df[col] = pd.to_numeric(df[col], downcast="float")
    after_mem = df.memory_usage(deep=True).sum() / (1024 * 1024)
    ratio = (before_mem - after_mem) / before_mem * 100
    log.append(
        f"Optimized numeric cols: {before_mem:.2f}MB → {after_mem:.2f}MB (↓{ratio:.1f}%)"
    )
    return df


# ---------------- Main ----------------
def main():
    log = []
    files = [
        os.path.join(DATA_FOLDER, f)
        for f in os.listdir(DATA_FOLDER)
        if f.endswith(".csv")
    ]
    dfs = [safe_read_csv(f) for f in files]
    df = pd.concat(dfs, ignore_index=True)
    log.append(f"Merged {len(files)} files: {df.shape}")

    df = clean_dataframe(df, log)
    df_final = feature_selection(df, log)
    df_final = optimize_numeric(df_final, log, decimals=2)

    df_final.to_csv(OUT_FILE, index=False, encoding="utf-8-sig")
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write("\n".join(str(x) for x in log))

    print("✅ Saved cleaned dataset:", OUT_FILE, df_final.shape)
    print("📊 Validation report written:", REPORT)


if __name__ == "__main__":
    main()
