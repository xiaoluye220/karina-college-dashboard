
import streamlit as st
import pandas as pd

# Title
st.title("🎓 Karina's College Match Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("Karina_College_List_Complete_All_Fits.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filter Colleges")

fit_min = st.sidebar.slider("Minimum Writing Fit (1–5)", 1, 5, 3)
theater_min = st.sidebar.slider("Minimum Theater Fit (1–5)", 1, 5, 3)
category = st.sidebar.multiselect("Category", options=df["Category"].unique(), default=list(df["Category"].unique()))
ed_type = st.sidebar.multiselect("ED/EA Type", options=df["ED/EA Type"].dropna().unique(), default=list(df["ED/EA Type"].dropna().unique()))

# Apply filters
filtered_df = df[
    (df["Fit for Writing (1-5)"] >= fit_min) &
    (df["Fit for Theater (1-5)"] >= theater_min) &
    (df["Category"].isin(category)) &
    (df["ED/EA Type"].isin(ed_type))
]

# Show results
st.markdown(f"### 🎯 Showing {len(filtered_df)} Colleges Matching Criteria")
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

# Optional: Download link
st.download_button(
    label="📥 Download Filtered Results as CSV",
    data=filtered_df.to_csv(index=False),
    file_name="Filtered_Colleges.csv",
    mime="text/csv"
)
