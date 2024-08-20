# Imports
import pandas as pd
import os

from config.database import ConfigureDatabase

from .engine.trainer import ModelTrainer
from .variables.train import train_sql_script, train_delta_year, train_delta_day, model_path

from . import DATA_DIR
from . import MODELS_DIR

def train_pipeline() -> None:

    # Get Database connection
    print("\n    [INFO] Connect to database ...")
    configure_database = ConfigureDatabase()
    configure_database.get_environment_variables()
    connection = configure_database.get_connection()
    cursor = configure_database.get_cursor()

    # Take arguments from console
    print("\n    [INFO] Reading processed data from SQL ...")

    with open(os.path.join(DATA_DIR, 'train.sql'), 'r') as f:
        TRAIN_SQL = f.read()
        TRAIN_SQL = TRAIN_SQL.replace(':delta_year', '%s').replace(':end_day', '%s')

    cursor.execute(TRAIN_SQL, (str(train_delta_year) + ' year', str(train_delta_day) + ' day'))  
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
    configure_database.close()


if __name__ == "__main__":
    train_pipeline()
