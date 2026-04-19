import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("data/data.csv")

X = df.drop("eta", axis=1)
y = df["eta"]

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "model/model.pkl")

print("Model trained & saved!")