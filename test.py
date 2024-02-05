import pandas as pd
import ml_backend

df = pd.read_csv('D.csv')
for i in range(12):
    for j in ml_backend.analyze_data("indsif",df.iloc[i:i+1]):
        print(j)