import streamlit as st
import sqlite3
import pandas as pd

# Title
st.title("Baseball Season Stats Dashboard")

# Connect to SQLite
conn = sqlite3.connect("assignment14/baseball_data.db")

# Load tables
df_years = pd.read_sql_query("SELECT * FROM season_years", conn)
df_events = pd.read_sql_query("SELECT * FROM season_events", conn)
df_stats = pd.read_sql_query("SELECT * FROM season_statistics", conn)

# Join tables using YearID and Event
merged = df_stats.merge(df_events, on=["YearID", "Event"]).merge(df_years, on="YearID")

# Sidebar filters
st.sidebar.header("Filter Options")
year_selected = st.sidebar.selectbox("Select Year", sorted(df_years["Year"].unique()))
event_keyword = st.sidebar.text_input("Search Event Keyword", "")

# Filter data
filtered = merged[merged["Year"] == year_selected]
if event_keyword:
    filtered = filtered[filtered["Event"].str.contains(event_keyword, case=False)]

# Show table
st.subheader(f"Stats for {year_selected}")
st.dataframe(filtered[["Team", "Event", "Value"]])

# Visual 1: Top 10 Teams by Total Stat Count
st.subheader("Top 10 Teams by Total Numeric Stat Values")
filtered["NumericValue"] = pd.to_numeric(filtered["Value"], errors="coerce")
team_totals = filtered.groupby("Team")["NumericValue"].sum().sort_values(ascending=False).head(10)
st.bar_chart(team_totals)


# Visual 2: Number of Stats Per Team
st.subheader("Number of Stats Per Team")
team_counts = filtered["Team"].value_counts()
st.bar_chart(team_counts)

# Visual 3: Event Count Per Year
st.subheader("Number of Events Each Year")
event_count = df_events.merge(df_years, on="YearID").groupby("Year")["Event"].count().reset_index()
st.area_chart(event_count.set_index("Year"))