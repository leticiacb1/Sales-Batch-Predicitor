# # Take arguments from console
# print("\n    [INFO] Reading new data ...")
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