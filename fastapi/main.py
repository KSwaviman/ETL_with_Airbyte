from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/data")
def read_data():
    df = pd.read_csv("/app/data/transformed_products.csv")
    return df.to_dict()
