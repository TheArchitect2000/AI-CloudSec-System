# Team 11 Cleaned Data

## Data Sources:

### BotNeTIoT
https://www.kaggle.com/datasets/azalhowaide/iot-dataset-for-intrusion-detection-systems-ids/data


### TON IoT
https://research.unsw.edu.au/projects/toniot-datasets


## Notebooks:
There are 2 notebooks for data analysis, and one for data creation creation. 


### team11_BoTNeTIoT-L01.ipynb
Used to clean data and split test/train data for the BotNetIoT dataset. 
This reviews statistical features of the dataset as shown in the notebook.



### team11_TON_IoT.ipynb
Used to clean data and split test/train data for the TON IoT dataset. 
This trims the dataset by removing repeating values that have no correlation, as well as dropping values that are not essential to the model.



### team11_create_clean_TON_IoT_unsw_edu_au.ipynb
This notebook is used to **generate data** for the TON IoT dataset.
To use this notebook:
1. Download TON IoT dataset from the original source, specifically the "Processed_Network_dataset" folder.
2. Create a new folder inside "tep2-Generated-Security-ML-Models" called "raw."
3. Move the "Processed_Network_dataset" inside the new raw folder.
4. Run the notebook. A new dataset will be written in the "Step1-Datasets-Feature-Engineering"
5. Delete the raw folder.



