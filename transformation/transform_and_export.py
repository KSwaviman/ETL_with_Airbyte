import psycopg2
import pandas as pd
import numpy as np
import json
from sqlalchemy import create_engine

# Create SQLAlchemy engine
engine = create_engine('postgresql+psycopg2://etl_user:password@localhost/etl_db')

# Query to extract data
query = """
SELECT
    id,
    sku,
    tags,
    brand,
    price,
    stock,
    title,
    rating,
    weight,
    reviews,
    category,
    dimensions,
    description,
    "discountPercentage",
    _airbyte_raw_id,
    _airbyte_extracted_at
FROM
    public."DummyJSON_Source"
"""

# Read data into a DataFrame
df = pd.read_sql_query(query, engine)

# 1. Keep only the specified columns (already selected in the query)

# 2. Remove [ and ] from the tags column
df['tags'] = df['tags'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)

# 3. Create Average_Rating column from reviews
def calculate_average_rating(reviews):
    try:
        review_list = reviews if isinstance(reviews, list) else json.loads(reviews)
        if review_list:
            return np.round(np.mean([review['rating'] for review in review_list]), 1)
        else:
            return np.nan
    except:
        return np.nan

df['Average_Rating'] = df['reviews'].apply(calculate_average_rating)

# 4. Transform dimensions to Dim column
def format_dimensions(dimensions):
    try:
        dim = dimensions if isinstance(dimensions, dict) else json.loads(dimensions)
        return f"{dim['depth']:.1f} X {dim['width']:.1f} X {dim['height']:.1f}"
    except:
        return np.nan

df['Dim'] = df['dimensions'].apply(format_dimensions)

# 5. Calculate FinalPrice column
df['FinalPrice'] = df.apply(lambda row: row['price'] * (1 - row['discountPercentage'] / 100), axis=1)

# 6. Round price-related columns to 1 decimal point
df['price'] = df['price'].round(1)
df['discountPercentage'] = df['discountPercentage'].round(1)
df['FinalPrice'] = df['FinalPrice'].round(1)

# Drop the original dimensions column
df = df.drop(columns=['dimensions'])

# Save the transformed data to a CSV file in the specified directory
df.to_csv('.\\data\\transformed_products.csv', index=False)

print("Data transformed and exported to .\\data\\transformed_products.csv")
