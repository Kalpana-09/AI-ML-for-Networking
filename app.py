# app.py

import streamlit as st
import pandas as pd
import joblib
from feature_extraction import required_features

# Load trained model
model = joblib.load("rf_model.pkl")


st.title(" Network Attack Type Classifier")
st.write("Upload a network flow CSV to detect attack types like **DDoS**, **PortScan**, and more.")

# File uploader
file = st.file_uploader(" Upload a CSV file", type="csv")

if file:
    try:
        df = pd.read_csv(file)

        # Match available features
        matched = [f for f in required_features if f in df.columns]
        missing = [f for f in required_features if f not in df.columns]

        # Clean output message
        st.success(f" {len(matched)} of {len(required_features)} required features found.")
        
        if missing:
            st.warning(" Some features were missing and filled with default values (0).")
            for f in missing:
                df[f] = 0.0

        # Ensure proper order
        df_model = df[required_features].copy()

        # Clean bad values
        df_model.replace([float('inf'), -float('inf')], pd.NA, inplace=True)
        df_model.dropna(inplace=True)

        if df_model.empty:
            st.error(" No valid rows to predict after cleaning.")
        else:
            preds = model.predict(df_model)
            df['Prediction'] = preds

            st.success(" Prediction successful!")

            # Summary table
            st.subheader(" Attack Type Summary")
            summary = df['Prediction'].value_counts().reset_index()
            summary.columns = ['Attack Type', 'Count']
            st.dataframe(summary)

            # Small preview
            st.subheader(" Sample Prediction Results")
            st.dataframe(df[['Prediction']].head(100))
            st.caption("Showing top 100 predictions. You can download the full results below.")

            # Download button
            st.download_button(" Download Full Predictions CSV", df.to_csv(index=False), "predicted_output.csv")

    except Exception as e:
        st.error(f" Error: {str(e)}")
