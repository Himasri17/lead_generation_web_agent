import streamlit as st
import pandas as pd

from src.scoring import calculate_score
from src.utils import load_data, save_ranked_data

# Page settings
st.set_page_config(page_title="Lead Scoring Dashboard", layout="wide")

st.title("🔬 3D In-Vitro Lead Generation Dashboard")

# Load data
df = load_data("data/leads_dataset.csv")

# Calculate scores
df["Probability_Score"] = df.apply(calculate_score, axis=1)

# Rank leads
df = df.sort_values(by="Probability_Score", ascending=False)
df["Rank"] = range(1, len(df) + 1)

# Save output
save_ranked_data(df, "output/ranked_leads.csv")

# Search filter
search = st.text_input("🔍 Search by Location / Company / Title")

if search:
    df = df[df.apply(lambda row: search.lower() in row.astype(str).str.lower().to_string(), axis=1)]

# Display table
st.dataframe(df, use_container_width=True)

# Download button
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇ Download Ranked Leads (CSV)",
    data=csv,
    file_name="ranked_leads.csv",
    mime="text/csv"
)

st.success("Leads successfully ranked based on probability to work with 3D in-vitro models.")
