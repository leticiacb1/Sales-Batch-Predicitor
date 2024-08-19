# Imports
import pandas as pd

from config.database import ConfigureDatabase

from .engine.trainer import ModelTrainer
from .variables.train import train_sql_script, train_sql_params, model_path

def train_pipeline() -> None:

    # Get Database connection
    print("\n    [INFO] Connect to database ...")
    configure_database = ConfigureDatabase()
    configure_database.get_environment_variables()
    connection = configure_database.get_connection()
    cursor = configure_database.get_cursor()

    # Take arguments from console
    print("\n    [INFO] Reading processed data from SQL ...")

    with open(train_sql_script, 'r') as f:
        TRAIN_SQL = f.read()

    df = pd.read_sql_query(TRAIN_SQL, connection, params=train_sql_params)

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
    print(f"\n    [INFO] Saving model in {model_path} ... \n")
    trainer.save_model(model_path)

    # Close database connection
    configure_database.close_connection()


if __name__ == "__main__":
    train_pipeline()
