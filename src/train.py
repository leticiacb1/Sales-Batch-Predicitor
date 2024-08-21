# Imports
import pandas as pd
import os

from config.database import ConfigureDatabase

from .engine.trainer import ModelTrainer
from .variables.train import create_sql_script, select_sql_script, train_delta_year, train_delta_day, model_path

from . import DATA_DIR
from . import MODELS_DIR

def train_pipeline() -> None:

    # Get Database connection
    print("\n    [INFO] Connect to database ...")
    configure_database = ConfigureDatabase()
    configure_database.get_environment_variables()
    connection = configure_database.get_connection()
    cursor = configure_database.get_cursor()

    # Execute SQL Script
    print(f"\n    [INFO] Reading processed data from SQL on {create_sql_script} and {select_sql_script} ...")

    with open(os.path.join(DATA_DIR, create_sql_script), 'r') as f:
        CREATE_SQL = f.read()
        CREATE_SQL = CREATE_SQL.replace(':delta_year', '%s').replace(':delta_day', '%s')
    cursor.execute(CREATE_SQL, (train_delta_year, train_delta_day)) 
    connection.commit()

    with open(os.path.join(DATA_DIR, select_sql_script), 'r') as f:
        SELECT_SQL = f.read()
    cursor.execute(SELECT_SQL)
    
    df = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

    # Instantiate a model trainer
    print("\n    [INFO] Creating ModelTrainer() ...")
    trainer = ModelTrainer(df)

    # Prepare data for training
    print("\n    [INFO] Prepare data for training ...")
    trainer.prepare_data()

    # Train the model
    print("\n    [INFO] Start training ...")
    trainer.train_model()

    # Saving model
    model_file_path = str(MODELS_DIR) + '/' + model_path
    print(f"\n    [INFO] Saving model in {model_file_path} ... \n")
    trainer.save_model(model_file_path)

    # Close database connection
    print("\n    [INFO] Closing database connection ...")
    configure_database.close()

if __name__ == "__main__":
    train_pipeline()
