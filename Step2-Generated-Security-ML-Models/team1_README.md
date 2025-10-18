About

(UNSW-NB15)
. Description: Modern intrusion detection dataset (9 attack families).
Size: ~2.5M records.
Features: 49 features (packet & flow statistics).
Download:
Official: https://research.unsw.edu.au/projects/unsw-nb15-dataset
Kaggle Mirror: https://www.kaggle.com/datasets/alextamboli/unsw-nb15
https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset/data


(CIC-IDS2017)
. Description: Labeled intrusion detection dataset (benign + multiple attacks).
Size: ~2.8M records (CSV + PCAP).
Features: ~80 flow-based features (protocols, flags, packet sizes).
Download:
 - Official: https://www.unb.ca/cic/datasets/ids-2017.html


We merged the individual CSV files into one raw file and applied the cleaning and feature functions.
Additionally, after generating the cleaned CSV file, we compress the files to CSV.ZIP file to reduce size to 25%, limit the size under 25MB for GitHub upload.
The csv.zip file is for model training.


CIC-IDS2017 — Cleaning + Feature
------------------------------------------------------------------------
1) Load all CIC-IDS2017 CSVs from INPUT_DIR (glob patterns provided)
2) Clean:
   - normalize column names
   - reduce benign dataset to fraction 1/3
   - replace 'Infinity', 'inf', 'NaN' strings -> NaN, then fill numerics with 0, strings with ""
   - drop duplicates
   - count Benign and other classes
   - normalize timestamps ('Timestamp' variants) to epoch/hour/weekday
3) Feature creation:
   - ratios: fwd/bwd packets & bytes (if columns present)
   - drop all the unused columns, specially the privacy sensitive datas, such as "IP, Time"
   - only keep 12 features highly correlative to the classes. These features are used for modeling
4) Encoding:
   - one-hot only a few categoricals (Protocol, Service, State), capped to Top-K to avoid explosion
5) Scaling:
   - Standard or MinMax on numeric columns (NumPy only)
6) Feature selection:
   - drop highly correlated (> 0.98 abs) columns
7) Dimensionality reduction:
   - PCA via NumPy (keep 95% variance)
8) Save:
   - cleaned CSV, summary_stats.csv, correlation_heatmap.png, pca_scatter.png
9) Merged and Compress to reduce the size of CSV file:
   -merged all cleaned CSV, set chunk = 500_00, compression 9 (highest compress level)
10) Split the data to x_test,x_train,y_test,y_train. ratio=0.3, 30% for testing, 70% for training
"""
UNSW-NB15— Cleaning + Feature
--------------------------------------
What this script does:
1) Load all NSW-NB15 CSVs from INPUT_DIR (glob patterns provided)
2) Clean:
   - normalize column names
   - reduce benign dataset to fraction 1/3
   - replace 'Infinity', 'inf', 'NaN' strings -> NaN, then fill numerics with 0, strings with ""
   - drop duplicates
   - count Benign and other classes for 9 attack families
3) Feature creation:
   - ratios: fwd/bwd packets & bytes (if columns present),drop out privacy sensitive data
   - identify features about 9 attack families
4) Encoding:
   - one-hot only a few categoricals (Protocol, Service, State), capped to Top-K to avoid explosion
5) Scaling:
   - Standard or MinMax on numeric columns
   - Generate correlation heatmap
6) Feature selection:
   - drop highly correlated (> 0.98 abs) columns
7) Dimensionality reduction:
   - PCA via NumPy (keep 95% variance)
8) Save:
   - cleaned CSV
9) Merged and Compress to reduce the size of CSV file:
   -merged all cleaned CSV, set chunk = 500_00, compression 9 (highest compress level)
10) Split the data to x_test,x_train,y_test,y_train. ratio=0.3, 30% for testing, 70% for training

Dependencies: pandas, numpy, matplotlib
