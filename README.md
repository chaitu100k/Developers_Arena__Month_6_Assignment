# Developers_Arena__Month_6_Assignment
It includes Developers Arena Internship month 6 assignment files

# 🚦 Traffic Flow Prediction System (DEPLOYMENT)

This repository contains a ready-to-submit data science project for **Traffic Flow Prediction**.
It includes Jupyter notebooks for data collection, cleaning, EDA, modeling, evaluation, and a simple dashboard/report.
A sample CSV dataset is included at `data/synthetic_traffic_dataset.csv`. Replace it with your dataset or provide the path
to your CSV in the notebooks where indicated.

## Structure
- `data/` - contains `synthetic_traffic_dataset.csv`
- `notebooks/` - Jupyter notebooks (data_collection.ipynb, cleaning_eda.ipynb, modeling.ipynb, LSTM_feature_engineering.ipynb, model_evaluation.ipynb, Model_Testing.ipynb, evaluation_dashboard.ipynb, Flask_Deployment.ipynb, Test_API(Notebook))
- `src/` - helper scripts (train.py, preprocess.py, predict.py)
- `report/` - contains a publish-ready PDF and markdown report

## How to use
1. Download the ZIP and extract.
2. Open notebooks in `notebooks/`. Each notebook includes a cell near the top where you can set `DATA_PATH`:
```python
# set your dataset path here (absolute or relative)
DATA_PATH = "data/synthetic_traffic_dataset.csv"
```
3. Run the notebooks in order:
   - `data_collection.ipynb` (examples to load data and optionally download from an online source)
   - `cleaning_eda.ipynb` (cleaning and exploratory plots)
   - `modeling.ipynb` (feature engineering and training an LSTM/LightGBM model)
   - `evaluation_dashboard.ipynb` (evaluation and streamlit dashboard example)
4. The `report/` folder contains a PDF report (if generated) and a markdown version you can edit.


## 📌 Overview
A real-time traffic flow forecasting system using LSTM networks.

## 📊 Dataset
Synthetic + multi-sensor traffic data with weather & anomaly features.

## 🧠 Model
- LSTM (Keras)
- Time-series feature engineering
- MAE, RMSE evaluation

## 🚀 Deployment
Flask-based API deployed on Hiroku.

## 🔗 Live Demo
https://Traffic-flow-prediction-system.herokuapp.com/

## 📂 Notebooks
- Data Collection
- EDA
- Feature Engineering
- Model Evaluation
- Deployment

## 👤 Author
Krishna Chaitanya Kollipara
