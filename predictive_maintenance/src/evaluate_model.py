import pandas as pd
from sklearn.metrics import mean_squared_error

pred = pd.read_csv("data/processed/predictions.csv")
rul = pd.read_csv("data/raw/RUL_FD001.txt", header=None)

pred = pred.groupby("engine_id").tail(1)

y_pred = pred["predicted_RUL"].values
y_true = rul[0].values

rmse = mean_squared_error(y_true, y_pred) ** 0.5

print("Test RMSE:", rmse)