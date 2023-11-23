import streamlit as st
import pandas as pd
from datetime import datetime

# Sample DataFrame
data = {
    'Date': pd.date_range(start='2023-01-01', end='2023-01-10'),
    'Value': [i for i in range(1, 11)]
}

df = pd.DataFrame(data)

# Title for your app
st.title("Date Range Selector App")

# Add a date range selector
start_date = pd.to_datetime(st.date_input("Select start date", df['Date'].min(), key='start_date'))
end_date = pd.to_datetime(st.date_input("Select end date", df['Date'].max(), key='end_date'))

# %%
#start_date = pd.to_datetime('2023-01-03')
#end_date = pd.to_datetime('2023-01-05')

# Filter the DataFrame based on the selected date range
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Display the selected date range
st.write("Selected Date Range:", start_date, "to", end_date)

# Display the filtered DataFrame
st.write("Filtered DataFrame:")
st.write(filtered_df)


min_date = datetime.date(df['Date'].min())
max_date = datetime.date(df['Date'].max())

st.slider("Select a date range", min_value=min_date, max_value=max_date, value=(start_date, end_date), step=timedelta(days=1),label_visibility="visible")