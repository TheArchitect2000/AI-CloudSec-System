from airflow.sdk import chain, dag, task
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
import pickle

%%writefile ../../dags/airflow.py
# @dag(schedule_interval=timedelta(days=1), start_date=datetime(2023, 1, 1), catchup=False)
@dag
def ml_pipeline():
    data = data_load()
    model = train_model(data)
    evaluate_model(model)

    @task
    def data_load():
        import kagglehub
        path = kagglehub.dataset_download("camnugent/california-housing-prices")
        df = pd.read_csv(path + "/housing.csv")
        return df

    @task
    def train_model(df):
        df.dropna(inplace=True)
        xtrain, xtest, ytrain, ytest = train_test_split(df.drop(columns=['median_house_value','ocean_proximity']),
                                                        df['median_house_value'], test_size=0.3, random_state=42)
        model = LinearRegression()
        model.fit(xtrain, ytrain)
        return model, xtest, ytest

    @task
    def evaluate_model(model_data):
        model, xtest, ytest = model_data
        pred = model.predict(xtest)
        mse = mean_squared_error(ytest, pred)
        mae = mean_absolute_error(ytest, pred)
        r2 = r2_score(ytest, pred)
        print(f"mse: {mse}, mae: {mae}, r2: {r2}")
        return mse, mae, r2

ml_pipeline()

# %%
