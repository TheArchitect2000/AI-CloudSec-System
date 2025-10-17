# Team 2 — Dataset Cleaning and Optimization Summary

## 1. Data Source
- Original dataset: **CICIDS2017 network traffic dataset**  
- Original dataset URL:  http://cicresearch.ca/CICDataset/CIC-IDS-2017/Dataset/CIC-IDS-2017/CSVs/
- Merged 8 raw CSV files into a single cleaned dataset for Step 1.  
- All files located in `Step1-Datasets-Feature-Engineering/`.

---

## 2. Data Merge Overview
| Metric | Value |
|---------|-------|
| Raw files merged | 8 |
| Original shape | (3,119,345 rows, 85 columns) |
| After cleaning | (2,829,183 rows, 48 columns) |
| Rows removed | 290,162 (NaN + duplicate rows) |

---

## 3. Cleaning Steps and Logic

| Step | Operation | Details |
|------|------------|---------|
| 1 | Remove NaN and duplicate rows | 290,162 rows removed to ensure unique records by timestamp + flow ID. |
| 2 | Drop constant columns | 8 columns removed:<br>`Bwd PSH Flags`, `Bwd URG Flags`, `Fwd Avg Bytes/Bulk`, `Fwd Avg Packets/Bulk`, `Fwd Avg Bulk Rate`, `Bwd Avg Bytes/Bulk`, `Bwd Avg Packets/Bulk`, `Bwd Avg Bulk Rate`. |
| 3 | Drop IP/Timestamp columns | 3 columns (`Source IP`, `Destination IP`, `Timestamp`) removed for privacy and redundancy. |
| 4 | Remove low-variance features | 9 columns with variance < 1e-4 removed. |
| 5 | Remove highly correlated features | 17 columns with correlation > 0.95 removed to reduce redundancy. |
| 6 | Optimize numeric types | Converted `float64` → `float32`; memory usage ↓ **43.5 %** (466.14 MB → 263.58 MB). |

---

## 4. Optimization Summary
| Metric | Before | After | Reduction |
|---------|--------|-------|-----------|
| Numeric columns memory | 466.14 MB | 263.58 MB | ↓ 43.5 % |

---

## 5. Validation
- Dataset loads successfully with Pandas:  
  ```python
  import pandas as pd
  df = pd.read_csv("team2_TrafficLabellingClean.csv")
  print(df.shape)
