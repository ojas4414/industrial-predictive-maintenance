import pandas as pd

train_path = "data/raw/train_FD001.txt"
test_path = "data/raw/test_FD001.txt"

cols = ["engine_id","cycle","setting1","setting2","setting3"] + [f"sensor{i}" for i in range(1,22)]

train = pd.read_csv(train_path,sep="\s+",header=None)
test = pd.read_csv(test_path,sep="\s+",header=None)

train.columns = cols
test.columns = cols

max_cycle = train.groupby("engine_id")["cycle"].max()

train = train.merge(max_cycle,on="engine_id",suffixes=("","_max"))

train["RUL"] = train["cycle_max"] - train["cycle"]

train = train.drop(columns=["cycle_max"])

train.to_csv("data/processed/train_processed.csv",index=False)
test.to_csv("data/processed/test_processed.csv",index=False)

print("preprocessing finished")