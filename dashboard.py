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
table = pd.pivot_table(
    df,
    values='student_count',
    index=['week'],
    columns=['learning_modality'],
    aggfunc="sum",
    fill_value=0  # Fill missing values
).reset_index()

# Debugging pivot table
st.markdown("### Debugging the Pivot Table")
st.write("Pivot Table Columns:")
st.write(table.columns)

st.write("Sample Data from Pivot Table:")
st.dataframe(table.head())

# Ensure week column is properly formatted
table['week'] = pd.to_datetime(table['week'], errors='coerce')
st.write("Week Column Format After Pivoting:")
st.write(table['week'].head())

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

# Replace plot_line_chart with plot_real_line_chart
def plot_real_line_chart():
    st.markdown("### Line Chart with Real Data")
    fig, ax = plt.subplots()

    if 'week' in table and 'Hybrid' in table and 'In Person' in table and 'Remote' in table:
        ax.plot(table['week'], table['Hybrid'], label='Hybrid', marker='o')
        ax.plot(table['week'], table['In Person'], label='In Person', marker='x')
        ax.plot(table['week'], table['Remote'], label='Remote', marker='s')
        ax.set_title("Student Count by Learning Modality")
        ax.set_xlabel("Week")
        ax.set_ylabel("Student Count")
        ax.legend()
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.write("Required columns are missing from the pivot table.")

# Call the function
plot_real_line_chart()



