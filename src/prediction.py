# Imports
import pandas as pd
import os

from config.database import ConfigureDatabase

from .engine.predictor import ModelPredictor
from .variables.prediction import create_sql_script, generate_sql_script, proccess__sql_script , start_store_id, end_store_id, days_in_future

from . import DATA_DIR
from . import MODELS_DIR


def process_predict_data():
    ...

def predict_pipeline():

    # Get Database connection
    print("\n    [INFO] Connect to database ...")
    configure_database = ConfigureDatabase()
    configure_database.get_environment_variables()
    connection = configure_database.get_connection()
    cursor = configure_database.get_cursor()

    # Execute SQL Script
    print("\n    [INFO] Reading predict data from SQL ...")

    print("\n      > Create table ...")

    with open(os.path.join(DATA_DIR, create_sql_script), 'r') as f:
        CREATE_SQL = f.read()

    cursor.execute(CREATE_SQL)
    connection.commit()

    print("\n      > Generate data ...")

    with open(os.path.join(DATA_DIR, generate_sql_script), 'r') as f:
        GENERATE_SQL = f.read()
        GENERATE_SQL = GENERATE_SQL.replace(':num_days', days_in_future).replace(':start_id', start_store_id).replace(':end_id', end_store_id)

    cursor.execute(GENERATE_SQL)
    connection.commit()

    print("\n      > Proccess data ...")

    with open(os.path.join(DATA_DIR, proccess__sql_script), 'r') as f:
        PROCCESS_SQL = f.read()

    cursor.execute(PROCCESS_SQL)

    df = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
    predict_df = df.drop('date_sale', axis=1)
    print(predict_df.head(3))

    # Instantiate processor
    print("\n    [INFO] Creating ModelPredictor() ...")
    predictor = ModelPredictor()


    # Close database connection
    configure_database.close()

if __name__ == "__main__":
    predict_pipeline()


    # df_predict = pd.read_parquet(data_predict_path)

# # Instantiate processor
# print("\n    [INFO] Creating ModelPredictor() ...")
# predictor = ModelPredictor()

# # Read model
# print("\n    [INFO] Read model ...")
# predictor.read_model(model_pickle_path = model_path)

# # Make prediction
# print("\n    [INFO] Make prediction ...")
# predictor.predict(X_test = df_predict)

# print("\n    [INFO] Predict value : \n")
# Y_prediction = predictor.get_y_prediction()
# print(f"{Y_prediction} \n")

# # Save prediction
# prediction_date = data_predict_path.split('predict')[1][1:].split('.')[0]
# prediction_path = "../data/predict-done-" + prediction_date + ".parquet"
# predictor.save_prediction(prediction_path=prediction_path)

