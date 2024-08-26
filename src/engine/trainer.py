# System
import sys
import importlib

# File
import pickle

# Data
import pandas as pd

# Typing
from typing import Tuple

# Model
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from src.variables.train import model_n_estimators, model_random_state

class ModelTrainer():

    def __init__(self, df):
        self._df = df
        self.model = RandomForestRegressor(n_estimators=model_n_estimators, random_state=model_random_state)

        self.one_hot_enc = None

        self.X_train = None
        self.Y_train = None

        self.X_test = None
        self.Y_test = None

    def show_info(self) -> None:
        print("\n------------------------------ ")
        print("\n ------- Model Trainer ------- \n")
        print("------------------------------ ")
        print("\n    [MODEL]")
        print(f"    {self.model}\n")
        print(f"    [X__train] \n {self.X_train}\n")
        print(f"    [Y__train] \n {self.Y_train}\n")
        print(f"    [X_test] \n {self.X_test}\n")
        print(f"    [Y_test] \n {self.Y_test}\n")
        print("\n ------------------------------ \n")

    def get_split_data(self) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
        return self.X_train, self.Y_train, self.X_test, self.Y_test

    def prepare_data(self, target_column_name: str = "total_sales", test_size: int = 0.3, random_state: int = 1912) -> None:
        """
            Spli data for training
        """

        if self._df.empty:
            raise ValueError("\n    [ERROR] Dataframe is empty ...")
    
        X = self._df.drop(target_column_name, axis=1)
        y = self._df[target_column_name]

        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

    def train_model(self) -> None:
        """
        Trains the model using the prepared training data.
        """
        if self.X_train is None or self.Y_train is None:
            raise ValueError("Training data has not been prepared. Call 'prepare_data' first.")

        # Fit data in model
        self.model.fit(self.X_train, self.Y_train)

    def save_model(self, file_path: str) -> None:
        """
        Save model as a pickle file
        """
        with open(file_path, "wb") as f:
            pickle.dump(self.model, f)
    