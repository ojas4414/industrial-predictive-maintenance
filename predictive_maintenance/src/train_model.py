import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

data = pd.read_csv("data/processed/train_features.csv")

X = data.drop(columns=["RUL","engine_id","cycle"])
y = data["RUL"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = RandomForestRegressor(n_estimators=70,n_jobs=-1)

model.fit(X_train,y_train)

pred = model.predict(X_test)

rmse = mean_squared_error(y_test,pred) ** 0.5

print("RMSE:",rmse)

joblib.dump(model,"models/rul_model.pkl")