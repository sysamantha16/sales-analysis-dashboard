
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Data Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload your sales_data.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=["Sale_Date"])

    st.subheader("📌 Raw Data")
    st.dataframe(df.head())

    # Filter options
    with st.sidebar:
        st.header("Filters")
        selected_region = st.multiselect("Select Region", options=df["Region"].dropna().unique())
        selected_category = st.multiselect("Select Product Category", options=df["Product_Category"].dropna().unique())

    filtered_df = df.copy()
    if selected_region:
        filtered_df = filtered_df[filtered_df["Region"].isin(selected_region)]
    if selected_category:
        filtered_df = filtered_df[filtered_df["Product_Category"].isin(selected_category)]

    # Profit column
    filtered_df["Profit"] = (filtered_df["Unit_Price"] - filtered_df["Unit_Cost"]) * filtered_df["Quantity_Sold"]

    # Charts
    '''st.subheader("📈 Total Sales by Product Category")
    sales_by_category = filtered_df.groupby("Product_Category")["Sales_Amount"].sum().sort_values(ascending=False)
    st.bar_chart(sales_by_category)'''

    # Example - Total Sales by Product Category
    fig, ax = plt.subplots()
    sns.barplot(x='Product_Category', y='Sales_Amount', data=df_filtered, ax=ax)
    st.pyplot(fig)

    st.subheader("🧭 Average Discount by Customer Type")
    discount_by_customer = filtered_df.groupby("Customer_Type")["Discount"].mean()
    fig1, ax1 = plt.subplots()
    ax1.pie(discount_by_customer, labels=discount_by_customer.index, autopct="%1.1f%%")
    ax1.axis("equal")
    st.pyplot(fig1)

    st.subheader("📉 Sales Over Time")
    if "Sale_Date" in filtered_df.columns:
        sales_over_time = filtered_df.groupby("Sale_Date")["Sales_Amount"].sum()
        st.line_chart(sales_over_time)

    # Download cleaned file
    st.subheader("⬇️ Download Cleaned Data")
    st.download_button("Download CSV", filtered_df.to_csv(index=False), "cleaned_sales_data.csv", "text/csv")

else:
    st.info("Please upload a CSV file to get started.")
