import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from scipy.stats import pearsonr

# Streamlit App Title
st.set_page_config(page_title="Sales Correlator", layout="wide")
st.title("📊 Sales Correlator: Analyze Revenue Correlations")

# Sidebar for File Upload
st.sidebar.header("Upload Your Sales Dataset")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# Sidebar Instructions
st.sidebar.markdown("""
### Instructions:
1. Upload your sales dataset in CSV format.
2. The application will process the file, encode categorical variables, and display the correlation results.
3. Explore statistical significance of correlations.
""")

if uploaded_file:
    # Load the uploaded CSV
    data = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    
    # Display raw data
    st.subheader("Raw Dataset Preview")
    st.dataframe(data.head())
    
    # Sidebar for Column Selection
    st.sidebar.header("Settings")
    categorical_columns = st.sidebar.multiselect(
        "Select Categorical Columns to Encode",
        options=data.select_dtypes(include=["object"]).columns,
        default=["branch", "city", "customer_type", "gender", "product_category"]
    )
    
    exclude_columns = st.sidebar.multiselect(
        "Select Columns to Exclude",
        options=data.columns,
        default=["sale_id", "product_name"]
    )
    
    # Encode categorical variables
    data_encoded = data.copy()
    for col in categorical_columns:
        data_encoded[col] = pd.factorize(data[col])[0]
    
    # Drop excluded columns
    data_encoded = data_encoded.drop(columns=exclude_columns, axis=1)
    
    # Correlation Calculation
    correlation_matrix = data_encoded.corr()
    
    # Heatmap Plot
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
    st.pyplot(fig)
    
    # Select Target Variable
    st.sidebar.header("Analyze Correlations")
    target_variable = st.sidebar.selectbox(
        "Select Target Variable for Correlation Analysis",
        options=data_encoded.columns,
        index=list(data_encoded.columns).index("total_price") if "total_price" in data_encoded.columns else 0
    )
    
    # Display Key Correlations
    correlations = correlation_matrix[target_variable].sort_values(ascending=False)
    st.subheader(f"Key Correlations with `{target_variable}`")
    st.write(correlations)
    
    # Statistical Significance Analysis
    st.subheader("Statistical Significance Test")
    strongest_feature = correlations.index[1]  # Skip the target variable itself
    strongest_correlation = correlations[1]
    
    x = data_encoded[target_variable]
    y = data_encoded[strongest_feature]
    correlation_coefficient, p_value = pearsonr(x, y)
    
    # Display Results
    st.write(f"**Strongest Feature**: `{strongest_feature}`")
    st.write(f"**Correlation Coefficient**: {strongest_correlation:.2f}")
    if abs(strongest_correlation) >= 0.7:
        st.markdown("✅ **Strong Correlation**")
    else:
        st.markdown("❌ **Not a Strong Correlation**")
    
    st.write(f"**P-value**: {'< 0.00001 (Highly Significant)' if p_value < 1e-5 else f'{p_value:.5f}'}")
    if p_value < 0.05:
        st.markdown("✅ **Statistically Significant**")
    else:
        st.markdown("❌ **Not Statistically Significant**")

else:
    st.warning("⚠️ Please upload a CSV file to proceed.")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Created by [Your Name]. Powered by Streamlit.")
