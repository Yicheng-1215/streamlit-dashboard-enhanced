def test_dummy_chart():
    st.markdown("### Test Dummy Line Chart")
    test_data = pd.DataFrame({
        'week': pd.date_range(start="2021-01-01", periods=5, freq='W'),
        'Hybrid': [10, 20, 30, 40, 50]
    })
    fig, ax = plt.subplots()
    ax.plot(test_data['week'], test_data['Hybrid'], label='Hybrid', marker='o')
    ax.set_title("Test Dummy Line Chart")
    ax.set_xlabel("Week")
    ax.set_ylabel("Hybrid Count")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

test_dummy_chart()




