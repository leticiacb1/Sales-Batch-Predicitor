# Imports
import pandas as pd
import os

from config.database import ConfigureDatabase

from .engine.predictor import ModelPredictor
from .variables.prediction import create_sql_script, generate_sql_script, proccess__sql_script , start_store_id, end_store_id, days_in_future, update__sql_script, model_path

from tqdm import tqdm

from . import DATA_DIR
from . import MODELS_DIR

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
    
    # Instantiate processor
    print("\n    [INFO] Creating ModelPredictor() ...")
    predictor = ModelPredictor()

    # Read model
    print("\n    [INFO] Read model ...")
    predictor.read_model(model_pickle_path = os.path.join(MODELS_DIR, model_path))

    # Make prediction
    print("\n    [INFO] Make prediction ...")
    _df = df.drop('date_sale', axis=1)

    # print(f" INPUT DATAFRAME: \n ")
    # print(_df)
    predictor.predict(X_test = _df)
    Y_prediction = predictor.get_y_prediction()
    df['total_sales'] = Y_prediction

    # Update table with predictions
    print("\n    [INFO] Update table with prediction ...\n")
    with open(os.path.join(DATA_DIR, update__sql_script), 'r') as f:
        UPDATE_SQL = f.read()
        UPDATE_SQL = UPDATE_SQL.replace(":predict_value", "%s").replace(":store_id", "%s").replace(":date",  "%s")
       
    updated_df = list(df.drop(["year", "month", "day", "weekday"], axis=1).itertuples(index=False, name=None))
    for row in tqdm(updated_df, desc="    Progress"):
        _store_id = str(row[0])
        _date = row[1].strftime('%Y-%m-%d')
        updated_total_sales = str(row[2])
    
        cursor.execute(UPDATE_SQL, (updated_total_sales, _store_id, "'" + _date + "'"))
        connection.commit()

    # Close database connection
    print("\n    [INFO] Closing database connection ...\n")
    configure_database.close()

if __name__ == "__main__":
    predict_pipeline()