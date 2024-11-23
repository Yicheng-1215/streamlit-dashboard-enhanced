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

# Debugging the pivot table
st.write("Pivot Table Data:")
st.dataframe(table)

# Check week column format
table['week'] = pd.to_datetime(table['week'], errors='coerce')
st.write("Week column format after pivoting:")
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

# Add Line Chart (using matplotlib)
def plot_line_chart():
    st.markdown("### Line Chart: Total Students Over Time")
    
    # Debugging
    st.write("Columns in table:")
    st.write(table.columns)
    
    st.write("Sample Data from Pivot Table:")
    st.dataframe(table.head())
    
    # Plotting
    fig, ax = plt.subplots()
    if 'week' in table and 'Hybrid' in table and 'In Person' in table and 'Remote' in table:
        ax.plot(table['week'], table['Hybrid'], label='Hybrid', marker='o')
        ax.plot(table['week'], table['In Person'], label='In Person', marker='x')
        ax.plot(table['week'], table['Remote'], label='Remote', marker='s')
        ax.set_title("Student Count by Learning Modality")
        ax.set_xlabel("Week")
        ax.set_ylabel("Student Count")
        ax.legend()
        plt.xticks(rotation=45)  # Rotate week labels for better visibility
        st.pyplot(fig)
    else:
        st.write("Required columns not found in the table. Check table structure.")

# Ensure the function is called
st.write("Plotting line chart...")
plot_line_chart()

# Test Line Chart with Dummy Data
def test_line_chart():
    st.markdown("### Test Line Chart")
    import matplotlib.pyplot as plt
    import pandas as pd

    # Dummy data
    test_data = pd.DataFrame({
        'week': pd.date_range(start="2021-01-01", periods=10, freq='W'),
        'Hybrid': range(10),
        'In Person': [x * 2 for x in range(10)],
        'Remote': [x * 3 for x in range(10)]
    })
    
    fig, ax = plt.subplots()
    ax.plot(test_data['week'], test_data['Hybrid'], label='Hybrid', marker='o')
    ax.plot(test_data['week'], test_data['In Person'], label='In Person', marker='x')
    ax.plot(test_data['week'], test_data['Remote'], label='Remote', marker='s')
    ax.set_title("Test Line Chart with Dummy Data")
    ax.set_xlabel("Week")
    ax.set_ylabel("Value")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Call the test function
test_line_chart()


