# 🚀 team5_BoTNeTIoT-L01-MLflow Experiment

This notebook demonstrates a **complete MLOps pipeline** for training, tracking, and registering a machine-learning model on the **BoT-IoT intrusion detection dataset** using **MLflow** and **KaggleHub** for dataset management.

---

## 📘 Overview

The project focuses on detecting IoT network intrusions using the **BoTNeTIoT-L01 dataset**, applying preprocessing, feature engineering, model training, and experiment tracking.

**Key steps covered:**
1. **Dataset loading**
   - Checks for a local copy under
     `../Step1-Datasets-Feature-Engineering/team11_BotNeTIoT-L01_label_NoDuplicates.csv`
   - If missing, automatically loads from the Kaggle dataset
     [`azalhowaide/iot-dataset-for-intrusion-detection-systems-ids`](https://www.kaggle.com/datasets/azalhowaide/iot-dataset-for-intrusion-detection-systems-ids)
2. **Feature selection and correlation analysis**
3. **Data splitting** into training and testing sets
4. **Model training** using `RandomForestClassifier`
5. **Experiment tracking** with **MLflow**
6. **Model registration** in the MLflow Model Registry

---

## 🧩 Environment Setup

Install required dependencies:
```bash
pip install mlflow kagglehub scikit-learn pandas numpy matplotlib seaborn
