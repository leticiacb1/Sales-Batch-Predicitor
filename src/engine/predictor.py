# System
import sys

# Data
import pandas as pd

# Export
import pickle

class ModelPredictor():

    def __init__(self):
        self.Y_prediction = None
        self.model = None
        self.one_hot_enc = None
    
    def read_model(self, model_pickle_path: str) -> None:
        """
        Read a model.pkl file and saved in a attribute.
        """
        file = open(model_pickle_path, "rb")
        self.model = pickle.load(file)
        file.close()

    def save_prediction(self, prediction_path):
        self.Y_prediction = pd.DataFrame({'Prediction': self.Y_prediction})
        self.Y_prediction.to_parquet(prediction_path)

    def get_y_prediction(self) -> pd.Series:
        """
        Return prediction made by model.
        """
        if self.Y_prediction is None:
            raise ValueError("Y_prediction has not been prepared. Call 'predict' first.")
        return self.Y_prediction

    def predict(self, X_test: pd.DataFrame) -> None:
        """
        Predicts the target values for the test set.
        """
        self.Y_prediction = self.model.predict(X_test)