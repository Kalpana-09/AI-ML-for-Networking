# feature_extraction.py

import pandas as pd

# Core features used for training/testing
required_features = [
    'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',
    'Fwd Packet Length Max', 'Fwd Packet Length Min', 'Fwd Packet Length Mean',
    'Bwd Packet Length Max', 'Bwd Packet Length Min', 'Bwd Packet Length Mean'
]

label_column = 'Label'

def load_and_clean_dataset(csv_path):
    print(f" Reading dataset from: {csv_path}")
    df = pd.read_csv(csv_path)

    # Match available features
    matched = [f for f in required_features if f in df.columns]
    print(f" Matched features: {matched} ({len(matched)} total)")

    if len(matched) < 4:
        raise ValueError(" Not enough matching features (need at least 4).")

    # Select required features + label if available
    if label_column in df.columns:
        df = df[matched + [label_column]]
    else:
        df = df[matched]

    # Clean invalid values
    df.replace([float('inf'), -float('inf')], pd.NA, inplace=True)
    df.dropna(inplace=True)

    print(f" Cleaned data shape: {df.shape}")
    return df


#  Optional: Run and save cleaned sample if run directly
if __name__ == "__main__":
    # Change this path to any dataset you want to test
    csv_path = r"C:\Network security\dataset\training_dataset_full.csv"

    df_cleaned = load_and_clean_dataset(csv_path)
    
    #  Save cleaned data as sample
    df_cleaned.to_csv("cleaned_sample.csv", index=False)
    print(" Saved cleaned sample to cleaned_sample.csv")
