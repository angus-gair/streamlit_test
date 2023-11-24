import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np

# Sample DataFrame with random data
np.random.seed(42)
data = {
    'Values': np.random.randn(100)
}

df = pd.DataFrame(data)

# Title for your app
st.title("Histogram with Line of Best Fit")

# Sidebar for customization
st.sidebar.header("Histogram Settings")
bin_count = st.sidebar.slider("Number of Bins", min_value=1, max_value=100, value=20)

# Create histogram
st.subheader("Histogram of Values")
sns.histplot(df['Values'], bins=bin_count, kde=True)

# Calculate and plot the line of best fit
mean_value = df['Values'].mean()
std_dev = df['Values'].std()
x_values = np.linspace(df['Values'].min(), df['Values'].max(), 100)
y_values = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_values - mean_value) / std_dev)**2)

st.line_chart(pd.DataFrame({'X': x_values, 'Y': y_values}), use_container_width=True)
