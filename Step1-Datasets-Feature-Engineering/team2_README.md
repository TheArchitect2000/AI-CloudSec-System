# Team 2 — Dataset Cleaning and Optimization (Step 1)

This document summarizes **Team 2’s Step 1: Dataset Cleaning and Optimization** for the **CICIDS2017** network traffic dataset. The goal of this stage was to merge multiple raw CSV files, remove missing and duplicate entries, drop constant and redundant features, and produce a memory-optimized dataset ready for Step 2 (Feature Engineering) and subsequent modeling.

All scripts were implemented in:
AI-CloudSec-System-1/Step1-Datasets-Feature-Engineering/

Main notebook: `team2_TrafficLabellingClean.ipynb`
Execution environment: Python 3.11, pandas 2.1.0, numpy 1.26.5, scikit-learn 1.3.2, jupyter 1.0.0.

---

## 1. Data Source
- Original dataset: **CICIDS2017 network traffic dataset**
- Official dataset URL: [http://cicresearch.ca/CICDataset/CIC-IDS-2017/Dataset/CIC-IDS-2017/CSVs/](http://cicresearch.ca/CICDataset/CIC-IDS-2017/Dataset/CIC-IDS-2017/CSVs/)
- Multiple daily CSVs were merged into one consolidated dataset for Team 2.
- Source folder:  C:\Users\hi\AI-CloudSec-System\data\traffic
  Step1-Datasets-Feature-Engineering/data/traffic/
- Cleaned output:  C:\Users\hi\AI-CloudSec-System-1\Step1-Datasets-Feature-Engineering
  Step1-Datasets-Feature-Engineering/team2_TrafficLabelling/team2_TrafficLabellingClean.csv

---

## 2. Data Merge Overview
| Metric | Value |
|---------|-------|
| Raw files merged | 6 of 8 (2 missing: Thursday and Friday) |
| Original shape | ≈ 3,119,345 rows × 85 columns |
| After cleaning | ≈ 2,369,199 rows × ~70 columns |
| Rows removed | NaN + duplicate rows per chunk |
| Output encoding | UTF-8-SIG |
| Output format | CSV |

---

## 3. Cleaning Steps and Logic
| Step | Operation | Description |
|------|------------|-------------|
| 1 | **Chunked reading (50 K rows per block)** | Read raw CSVs in chunks to prevent out-of-memory errors on local systems. |
| 2 | **Remove NaN and duplicate rows** | Dropped empty rows and duplicate entries within each chunk. |
| 3 | **Drop constant columns** | Removed 8 zero-variance features: `Bwd PSH Flags`, `Bwd URG Flags`, `Fwd Avg Bytes/Bulk`, `Fwd Avg Packets/Bulk`, `Fwd Avg Bulk Rate`, `Bwd Avg Bytes/Bulk`, `Bwd Avg Packets/Bulk`, `Bwd Avg Bulk Rate`. |
| 4 | **Drop IP / Timestamp columns** | Removed identifier columns for privacy and redundancy. |
| 5 | **Handle Inf / NaN values** | Replaced ±inf → NaN, then filled missing values with the column median (or 0 if all NaN). |
| 6 | **Optimize numeric types** | Converted `float64 → float32` and `int64 → int32` to reduce memory usage. |
| 7 | **Streaming write to CSV** | Appended each cleaned chunk directly to disk without keeping the full DataFrame in RAM. |

---

## 4. Optimization Summary
| Metric | Before | After | Reduction |
|---------|--------|-------|-----------|
| Numeric column memory | ≈ 466 MB | ≈ 263 MB | ↓ ≈ 43 % |
| Processing mode | Full in-memory | Chunked streaming | ✅ Memory safe |
| Peak RAM usage | > 8 GB | < 2 GB | ✅ Stable execution |

---

## 5. Validation
The dataset loads successfully using Pandas:

```python
import pandas as pd, os
df = pd.read_csv("team2_TrafficLabelling/team2_TrafficLabellingClean.csv", nrows=5)
print("Preview:", df.shape, "| Columns:", len(df.columns))
print("File size (MB):", round(os.path.getsize("team2_TrafficLabelling/team2_TrafficLabellingClean.csv")/(1024**2), 2))
```

Expected output:
```
✅ SAFE MODE done — rows written: 2369199
Preview: (5, 70) | Columns: 70
File size: ≈ 520 MB
```

---

## 6. Folder Structure
```
Step1-Datasets-Feature-Engineering/
│
├── data/traffic/                       # raw CICIDS2017 CSVs
├── team2_TrafficLabelling/             # cleaned output folder
│   └── team2_TrafficLabellingClean.csv
│
├── team2_TrafficLabellingClean.ipynb   # main cleaning notebook
├── requirements.txt
└── README.md
```

---

## 7. Team Information
- **Project:** AI-CloudSec-System
- **Course:** Operating Systems / Capstone Project
- **Team:** Group 2

**Team Members:**
- Jinyi Hu – 2106620 – j.hu3@student.fdu.edu
- Jia Min – 2107076 – j.min@student.fdu.edu
- Wenjie Xing – 2098805 – w.xing@student.fdu.edu

**Instructor:** Prof. Gholamreza Ramezan
**Institution:** Fairleigh Dickinson University (Vancouver)
**Date:** October 2025

---

## 8. License and Notes
- The cleaned dataset is intended for academic use under FDU coursework.
- This file will serve as the input for **Step 2: Feature Engineering**.
- Please cite as: *Team 2 – AI CloudSec System (2025).*

---

## Appendix – Environment Requirements
```
pandas==2.1.0
numpy==1.26.5
scikit-learn==1.3.2
jupyter==1.0.0
mlflow==2.8.3
apache-airflow==2.8.1
```

---

© 2025 Team 2 — AI CloudSec System · Fairleigh Dickinson University (Vancouver)
