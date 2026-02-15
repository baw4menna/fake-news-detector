# -*- coding: utf-8 -*-
"""
combine datasets
"""

import pandas as pd

# Load datasets
real = pd.read_csv("real_news_malaysia.csv")
fake = pd.read_csv("fake_news_malaysia.csv")

# Make sure both have the same column names
print("Real Columns:", real.columns)
print("Fake Columns:", fake.columns)

# Concatenate datasets
df = pd.concat([real, fake], ignore_index=True)

# Shuffle the combined dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the combined dataset
df.to_csv("malaysia_fake_news_dataset.csv", index=False)
print("Combined dataset saved as malaysia_fake_news_dataset.csv")
