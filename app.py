import streamlit as st
import pandas as pd

from src.scoring import calculate_score
from src.utils import load_data, save_ranked_data


# Page Configuration

st.set_page_config(
    page_title="3D In-Vitro Lead Generation Dashboard",
    layout="wide"
)

st.title("🔬 3D In-Vitro Lead Generation Dashboard")
st.write(
    "This dashboard identifies, enriches, and ranks potential leads based on "
    "their likelihood to collaborate on 3D in-vitro research models."
)


# Load Dataset

DATA_PATH = "data/leads_dataset.csv"

try:
    df = load_data(DATA_PATH)
except FileNotFoundError:
    st.error("Dataset not found. Please ensure data/leads_dataset.csv exists.")
    st.stop()

st.subheader("📊 Raw Lead Dataset")
st.dataframe(df, use_container_width=True)


# Scoring & Ranking

st.subheader("⚙️ Lead Scoring & Ranking")

# Calculate probability score
df["Probability_Score"] = df.apply(calculate_score, axis=1)

# Sort by score (descending)
df = df.sort_values(by="Probability_Score", ascending=False)

# Add rank column
df["Rank"] = range(1, len(df) + 1)

# Reorder columns for readability
preferred_order = [
    "Rank",
    "Name",
    "Title",
    "Company",
    "Probability_Score",
    "Funding_Stage",
    "Uses_InVitro_Tech",
    "Open_to_NAMs",
    "Recent_Publication",
    "Person_Location",
    "Company_HQ",
    "Email",
    "LinkedIn"
]

# Keep only columns that exist (safe)
final_columns = [col for col in preferred_order if col in df.columns]
df = df[final_columns]


# Save Ranked Output (Cloud-safe)

OUTPUT_PATH = "output/ranked_leads.csv"
save_ranked_data(df, OUTPUT_PATH)

st.success("✅ Leads scored, ranked, and saved successfully.")


# Display Ranked Leads

st.subheader("🏆 Ranked Leads")
st.dataframe(df, use_container_width=True)


# Download Button

st.subheader("⬇️ Download Ranked Leads")

csv_data = df.to_csv(index=False)

st.download_button(
    label="Download Ranked Leads as CSV",
    data=csv_data,
    file_name="ranked_leads.csv",
    mime="text/csv"
)

# Footer Note
st.markdown("---")
st.caption(
    "NOTE: This demo uses a synthetic dataset of 100 leads. "
    "The system is API-ready for Apollo.io integration, but uses CSV fallback "
    "for demo reliability."
)
