
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Performance Dashboard")

df = pd.read_csv("sales_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

# KPIs
total_revenue = df['Revenue'].sum()
total_profit = df['Profit'].sum()
top_region = df.groupby('Region')['Profit'].sum().idxmax()
top_category = df.groupby('Category')['Profit'].sum().idxmax()

st.markdown(f"### 💰 Total Revenue: ${total_revenue:,.0f}")
st.markdown(f"### 📈 Total Profit: ${total_profit:,.0f}")
st.markdown(f"### 🗺️ Top Region: {top_region}")
st.markdown(f"### 🛍️ Top Category: {top_category}")

# Monthly Trends
df['Month'] = df['Date'].dt.to_period('M').astype(str)
monthly = df.groupby('Month')[['Revenue', 'Profit']].sum().reset_index()
fig_line = px.line(monthly, x='Month', y=['Revenue', 'Profit'], title='Monthly Revenue & Profit')
st.plotly_chart(fig_line, use_container_width=True)

# Category Performance
cat = df.groupby('Category')[['Revenue', 'Profit']].sum().reset_index()
fig_bar = px.bar(cat, x='Category', y='Revenue', color='Profit', title='Revenue by Category')
st.plotly_chart(fig_bar, use_container_width=True)

# Region Pie Chart
region = df.groupby('Region')['Revenue'].sum().reset_index()
fig_pie = px.pie(region, names='Region', values='Revenue', title='Revenue by Region')
st.plotly_chart(fig_pie, use_container_width=True)
