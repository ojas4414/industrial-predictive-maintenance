import pandas as pd
import joblib

model = joblib.load("models/rul_model.pkl")

test = pd.read_csv("data/processed/test_features.csv")

X = test.drop(columns=["engine_id","cycle"])

pred = model.predict(X)

test["predicted_RUL"] = pred

result = test.groupby("engine_id").tail(1)

result.to_csv("data/processed/predictions.csv",index=False)

print(result[["engine_id","predicted_RUL"]])