About
(UNSW-NB15)
. Description: Modern intrusion detection dataset (9 attack families).
Features: 49 features (packet & flow statistics).

https://www.kaggle.com/datasets/alextamboli/unsw-nb15


(CIC-IDS2017)
. Description: Labeled intrusion detection dataset (benign + multiple attacks).
Features: ~80 flow-based features (protocols, flags, packet sizes).

 - https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset/data


We merged the individual CSV files into one raw file and applied the cleaning and feature functions. 
Additionally, after generating the cleaned CSV file, we compress the files to CSV.ZIP file to reduce size to 25%, limit the size under 25MB for GitHub upload. 
The csv.zip file is for model training.
