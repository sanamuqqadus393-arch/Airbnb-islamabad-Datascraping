import streamlit as st
import pandas as pd

st.set_page_config(page_title="Airbnb Dashboard", layout="wide")

# ---------- LOAD DATA ----------
df = pd.read_csv("airbnbIslamabadData.csv", index_col=0)

df.columns = df.columns.str.strip().str.lower()

# Clean price
df['price'] = df['price'].str.replace(r'[^0-9]', '', regex=True)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

df = df.dropna(subset=['price'])

# ---------- SIDEBAR ----------
st.sidebar.title("🔎 Filters")

min_price = int(df['price'].min())
max_price = int(df['price'].max())

price_range = st.sidebar.slider(
    "Select Price Range",
    min_price,
    max_price,
    (min_price, max_price)
)

search = st.sidebar.text_input("Search by Name")

filtered_df = df[
    (df['price'] >= price_range[0]) &
    (df['price'] <= price_range[1])
]

if search:
    filtered_df = filtered_df[
        filtered_df['name'].str.contains(search, case=False, na=False)
    ]

# ---------- HEADER ----------
st.title("🏡 Airbnb Islamabad Analytics")
st.caption("Interactive dashboard for Airbnb listings insights")

# ---------- METRICS ----------
col1, col2, col3 = st.columns(3)

col1.metric("Total Listings", len(filtered_df))
col2.metric("Average Price", f"${round(filtered_df['price'].mean(), 2)}")
col3.metric("Max Price", f"${int(filtered_df['price'].max())}")

# ---------- TOP LISTINGS ----------
st.subheader("🔥 Top 10 Most Expensive Listings")

top10 = filtered_df.sort_values(by='price', ascending=False).head(10)

st.dataframe(top10[['name', 'price']])

# ---------- CHARTS ----------
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Price Distribution")
    st.bar_chart(filtered_df['price'].head(50))

with col2:
    st.subheader("📊 Price Histogram")
    st.line_chart(filtered_df['price'].sort_values().reset_index(drop=True))

# ---------- TABLE ----------
st.subheader("📋 All Listings")
st.dataframe(filtered_df)

# ---------- FOOTER ----------
st.markdown("---")
# ___________Download _________
st.download_button(
    label="Download Data as CSV",
    data=filtered_df.to_csv(index=False),
    file_name='airbnb_data.csv',
    mime='text/csv'
)
st.caption("@sanamuqqadus | Data for educational purposes")
