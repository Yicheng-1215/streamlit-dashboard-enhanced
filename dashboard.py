import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Header and description
st.header("2024 AHI 507 Streamlit Example")
st.subheader("We are going to go through a couple different examples of loading and visualization information into this dashboard")

st.text("""In this Streamlit dashboard, we are going to focus on some recently released school learning modalities data from the NCES, for the years of 2021.""")

# Load the dataset
df = pd.read_csv("https://healthdata.gov/resource/a8v3-a3m3.csv?$limit=50000")

# Data cleaning
df['week_recoded'] = pd.to_datetime(df['week'])
df['zip_code'] = df['zip_code'].astype(str)

# Key metrics
col1, col2, col3 = st.columns(3)
col1.metric("Columns", df.shape[1]) 
col2.metric("Rows", len(df))
col3.metric("Number of unique districts/schools:", df['district_name'].nunique())

# Display dataset
st.dataframe(df)

# Pivot table for visualizations
table = pd.pivot_table(df, values='student_count', index=['week'],
                       columns=['learning_modality'], aggfunc="sum").reset_index()

# Bar charts
st.bar_chart(
    table,
    x="week",
    y="Hybrid",
)

st.bar_chart(
    table,
    x="week",
    y="In Person",
)

st.bar_chart(
    table,
    x="week",
    y="Remote",
)

# Add Line Chart (using matplotlib)
def plot_line_chart():
    st.markdown("### Line Chart: Total Students Over Time")
    fig, ax = plt.subplots()
    ax.plot(table['week'], table['Hybrid'], label='Hybrid', marker='o')
    ax.plot(table['week'], table['In Person'], label='In Person', marker='x')
    ax.plot(table['week'], table['Remote'], label='Remote', marker='s')
    ax.set_title("Student Count by Learning Modality")
    ax.set_xlabel("Week")
    ax.set_ylabel("Student Count")
    ax.legend()
    plt.xticks(rotation=45)  # Rotate week labels for better visibility
    st.pyplot(fig)

# Call the function to display the line chart
plot_line_chart()
