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
