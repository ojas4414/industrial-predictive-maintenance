import pandas as pd

train = pd.read_csv("data/processed/train_processed.csv")
test = pd.read_csv("data/processed/test_processed.csv")

drop_cols = ["engine_id","cycle"]
features = train.drop(columns=drop_cols + ["RUL"])

for col in features.columns:
    train[col+"_mean"] = train.groupby("engine_id")[col].transform(lambda x: x.rolling(5,1).mean())
    train[col+"_std"] = train.groupby("engine_id")[col].transform(lambda x: x.rolling(5,1).std())

    test[col+"_mean"] = test.groupby("engine_id")[col].transform(lambda x: x.rolling(5,1).mean())
    test[col+"_std"] = test.groupby("engine_id")[col].transform(lambda x: x.rolling(5,1).std())

train = train.fillna(0)
test = test.fillna(0)

train.to_csv("data/processed/train_features.csv",index=False)
test.to_csv("data/processed/test_features.csv",index=False)