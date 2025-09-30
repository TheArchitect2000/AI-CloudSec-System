# BoTNeTIoT-L01 Intrusion Detection Pipeline

This file contains a Jupyter Notebook implementation of a **machine learning and deep learning pipeline** for the **BoTNeTIoT-L01 dataset**.
> **Note:** For faster experimentation and lower memory use, the pipeline intentionally uses **only 100,000 rows** of the dataset.
The workflow covers preprocessing, feature selection, model training, evaluation, and model persistence.

---

##  Workflow Overview

### 1) Imports & Setup
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `TensorFlow/Keras`, `pickle`.
- Purpose: data handling, visualization, preprocessing, classical ML and deep learning models, and persistence.

---

### 2) Data Loading & Initial EDA
- Reads **`BotNeTIoT-L01-v2.csv`** into a DataFrame.
- Prints **columns**, `head()`, and `describe()`.
- Displays unique values for **Attack** and **Attack_subType**.
- Includes simple plots (count/pie) for attack and device distributions.

---

### 3) Categorical Encoding
- Converts categorical columns to numeric using **LabelEncoder**:
  - `Device_Name`
  - `Attack`
  - `Attack_subType`

---

### 4) Correlation & Leakage Check
- Correlation analysis shows **Attack** and **Attack_subType** are highly correlated with the target.
- Risk of **data leakage** if used as features.
- Decision: treat them as leakage-prone and **exclude** from modeling.

---

### 5) Prepared Dataset & Redundancy Reduction
- Loads cleaned file BoTNeTIoT-L01-v2-prepared.csv (restricted to the 100k subset during the notebook run).
- Defines a helper to **drop highly correlated features** (threshold > 0.95).
- Ensures reduced multicollinearity and better generalization.

---

### 6) Feature/Target Definition
- **Target**: `label`
  - `0` = Malicious/Attack
  - `1` = Normal
- **Features**: Remaining columns after dropping leakage-prone and redundant ones.

---

### 7) Train/Test Split & Scaling
- Splits dataset into **80% train / 20% test** (stratified).
- Applies **StandardScaler** to features.
- Saves reusable splits:
  - `X_train.csv`, `X_test.csv`
  - `X_train_scaled.csv`, `X_test_scaled.csv`

---

### 8) Models & Training

#### a) Random Forest (classical ML)
- Trains a **RandomForestClassifier** (`n_estimators=100` by default).
- Uses **feature importance** to rank and select top-N features.

#### b) Neural Network (MLP / Keras Sequential)
- Builds a **fully-connected Dense model** on scaled features.
- Compiles with:
  - Loss: `binary_crossentropy`
  - Metrics: `accuracy`, `AUC`, `precision`, `recall`
- Trains with validation split and/or test evaluation.

#### c) CNN (1D)
- Defines **`build_cnn(input_shape)`**:
  - `Conv1D(32, kernel_size=3, activation='relu')`
  - `MaxPooling1D(pool_size=2)`
  - `Conv1D(64, kernel_size=3, activation='relu')`
  - Dense output for binary classification.
- Compiles with:
  - Optimizer: `Adam`
  - Loss: `binary_crossentropy`
  - Metrics: `accuracy`, `AUC`, `precision`, `recall`
- Trains on **scaled features reshaped** to `(samples, n_features, 1)` with defined `epochs` and `batch_size`.

---

### 9) Evaluation & Visualization
- Metrics computed:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - AUC
- Visualization:
  - Confusion Matrix
  - ROC / Precision-Recall curves
- Compares results across **RF, MLP, CNN**.

---

### 10) Persistence
- Saves models for reuse:
  - `pickle` (for scikit-learn models)
  - `model.save(...)` (for Keras models)
- Persists dataset splits (`to_csv`) to avoid retraining.
