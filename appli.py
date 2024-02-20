import pandas as pd
import numpy as np   # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import matplotlib.pyplot as plt
import streamlit as st  # pip install streamlit
import plotly

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

st.title("SUPER MARKET DASHBOARD")
st.markdown("##")

with st.sidebar:
    st.subheader("Description")
    st.write("A supermarket is a self-service shop offering a wide variety of food, beverages and household products, organized into sections. This kind of store is larger and has a wider selection than earlier grocery stores, but is smaller and more limited in the range of merchandise than a hypermarket or big-box market.Data sources: Supermarket data comes from various sources such as point-of-sale (POS) systems, customer loyalty programs, inventory management systems, and online platforms. This data includes transaction records, product details, customer demographics, purchase history, and more.")

st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique(),
)

gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)


df_selection = df.query(
    "City == @city & Customer_type ==@customer_type & Gender == @gender"
)



total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)


left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")
    

with left_column:
    st.scatter_chart(df[['Rating','Unit price']])
    

with left_column:
    st.line_chart(df[['Rating','Unit price']])

st.markdown("""---""")


pie chart of gross income by City
    with col2:
        st.subheader("gross income by City")
        category_sales = filtered_df.groupby('City')['gross income'].sum().reset_index()
        fig = px.pie(category_sales, values='gross income', names='City')
        st.plotly_chart(fig, use_container_width=True)




























    











