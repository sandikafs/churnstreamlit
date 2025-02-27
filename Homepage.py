import streamlit as st
import pandas as pd

# Define dataset column descriptions
data = {
    "Column Name": [
        "CustomerID", "Churn", "Tenure", "PreferredLoginDevice", "CityTier",
        "WarehouseToHome", "PreferredPaymentMode", "Gender", "HourSpendOnApp",
        "NumberOfDeviceRegistered", "PreferedOrderCat", "SatisfactionScore",
        "MaritalStatus", "NumberOfAddress", "Complain", 
        "OrderAmountHikeFromLastYear", "CouponUsed", "OrderCount", 
        "DaySinceLastOrder", "CashbackAmount"
    ],
    "Description": [
        "Unique identifier for each customer.",
        "Customer churn status (0 = Retained, 1 = Churned).",
        "Duration (in months) the customer has been using the service.",
        "Most frequently used login device.",
        "Customer's city tier classification.",
        "Distance from the warehouse to the customer’s home.",
        "Most frequently used payment method.",
        "Customer's gender.",
        "Average time spent on the app.",
        "Number of registered devices.",
        "Most frequently ordered product category.",
        "Customer satisfaction score.",
        "Customer's marital status.",
        "Number of addresses linked to the customer.",
        "Complaint history (0 = No, 1 = Yes).",
        "Increase in order amount compared to last year.",
        "Number of coupons used.",
        "Total number of orders placed.",
        "Days since the last order.",
        "Total cashback received."
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)
# Convert DataFrame to HTML with custom styling
table_html = df.to_html(classes="dataframe", index=False, border=0)

# Set page configuration
st.set_page_config(
    page_title="Home - E-Commerce Churn Prediction",
    layout="wide"
)

# Add Sidebar Logo and Navigation Header
def add_sidebar_header():
    st.markdown("""
        <style>
            [data-testid="stSidebarNav"] {
                background-repeat: no-repeat;
                padding-top: 0px;
                background-position: 2px 2px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Navigation";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 10px;
                border-bottom: 2px solid #cccccc;
            }
        </style>
    """, unsafe_allow_html=True)

add_sidebar_header()  # Call function to add sidebar header

# Custom CSS for Styling
st.markdown("""
    <style>
        /* Global Background & Text */
        body, .main, .stApp {
            background-color: #ecf0f1 !important;  /* Light grey */
            color: white !important; /* Set all text to white */
        }

        /* Title Container */
        .title-container {
            background-color: #0c1c10;  /* Dark Green */
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            text-align: left;
            font-size: 32px;
            font-weight: bold;
            color: white !important;
        }

        /* Bubble Styling */
        .bubble {
            background-color: #4CAF50;  /* Green */
            border-radius: 15px;
            padding: 20px;
            padding-bottom: 10px !important;
            margin: 0px;
            margin-top: 10px;
            margin-bottom: 20px !important;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            color: white !important;
            font-size: 16px;
            line-height: 1.6;
            font-weight: normal;
            min-width: 90%; 
            max-width: 250px; /* Set a max width for responsiveness */
        }    

        /* Button Styling */
        .bubble-button {
            display: inline-block;
            padding: 10px 20px;
            border-radius: 25px;
            background-color: #4CAF50; /* Green */
            color: white !important;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
            margin-top: 10px;
        }
        .bubble-button:hover {
            background-color: #45a049;
            box-shadow: 3px 3px 7px rgba(0,0,0,0.4);
        }

        /* Custom Table Styling */
        .custom-table-container {
            background-color: #4CAF50;  /* Green background */
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        }
        
        .custom-table-container table {
            width: 100%;
            border-collapse: collapse;
            background-color: #ecf0f1 !important; /* Light background for table */
            color: black !important;
            border-radius: 10px;
        }
        
        .custom-table-container th, .custom-table-container td {
            padding: 10px;
            border: 1px solid #ddd;
        }
        
        .custom-table-container th {
            background-color: #2c3e50; /* Darker header */
            color: white;
        }

        /* Light background for the table */
        .dataframe { 
            background-color: white !important;
            color: black !important;
        }
        
        /* Light gray for header */
        .dataframe th {
            background-color: #f0f0f0 !important;
            color: black !important;
        }
        
        /* Alternating row colors */
        .dataframe tr:nth-child(even) {
            background-color: #f9f9f9 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title with Green Background
st.markdown('<div class="title-container">📊 E-Commerce Customer Churn Analysis and Prediction</div>', unsafe_allow_html=True)

# Create two columns for the Bubble and Image
col1, col2 = st.columns([1, 0.8]) 

# Description Inside a Green Bubble
with col1:
    st.markdown("""
        <div class="bubble">
            <h3>🔥 Welcome to Customer Churn Prediction</h3>  
            <p>This tool uses machine learning and data analysis to help businesses predict whether a customer is likely to churn.</p>  
            <p>With actionable insights, businesses can improve retention and revenue.</p>
        </div>
    """, unsafe_allow_html=True)

# Add Image in the Second Column
with col2:
    st.markdown("""
        <div style="margin-top: 10px;">
            <img src="https://www.cleartouch.in/wp-content/uploads/2022/11/Customer-Churn.png" 
                 style="max-width: 100%; height: auto; display: block; margin: auto;">
        </div>
        <div style="text-align: center;">
            <a href="https://www.cleartouch.in/blog/what-is-customer-churn-and-how-do-you-prevent-it/" 
               target="_blank" 
               style="color: #34585e; font-weight: bold; text-decoration: none;">
               Source
            </a>
        </div>
    """, unsafe_allow_html=True)

# Create Two Columns for "How it Works" and "Why Customer Churn is Important"
col1, colspace, col2 = st.columns([1.7, 0.2, 1.8]) 
with col1:
    # About the Dataset
    st.markdown("""
            <div class="bubble">
                <h3>📂 About the Dataset</h3>
                <p>This dataset contains historical customer data used for predicting churn in an e-commerce platform. Here's the dataset column descriptions:</p>
            </div>
    """, unsafe_allow_html=True)
    st.markdown(table_html, unsafe_allow_html=True)  # Render the table

# "Why Customer Churn is Important?" Section
with col2:
    st.markdown("""
        <div class="bubble">
            <h3>🔍 What is Customer Churn?</h3>
            <p>Customer churn or customer attrition is the percentage of customers that have stopped using your organization’s product or service.</p>
            <p>Customer churn is a critical metric for businesses because acquiring new customers is significantly more expensive than retaining existing ones.</p>  
            <p>Understanding churn helps businesses:</p>
            <ul>
                <li>📉 <strong>Reduce Revenue Loss</strong>: Every lost customer means lost revenue.</li>
                <li>💡 <strong>Improve Customer Experience</strong>: By analyzing churn reasons, businesses can improve their services.</li>
                <li>📊 <strong>Optimize Marketing Efforts</strong>: Predicting and preventing churn helps target marketing efforts better.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="bubble">
        <h3>🚀 How it Works (Step-by-Step Guide)</h3>
        <p>Follow these simple steps to get started:</p>
        <ul>
            <li><strong>Step 1: Go to Customer Prediction</strong><br>Click the button below or on the sidebar to begin.</li>
            <li><strong>Step 2: Analyze Prediction Results</strong><br>View insights and key factors influencing churn.</li>
            <li><strong>Step 3: Explore About Us</strong><br>Learn more about the team behind this project.</li>
        </ul>
        <p>Start predicting churn today and take control of your customer retention strategy!</p>
    </div>
    """, unsafe_allow_html=True)

    # Buttons using Streamlit API
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1:
        if st.button("➡️ Customer Churn Prediction"):
            st.switch_page("pages/1 Customer Churn Prediction.py")  # Use Streamlit's page navigation
    with col_btn2:
        if st.button("➡️ Customer Churn Analysis"):
            st.switch_page("pages/2 Customer Churn Analysis.py")  # Navigate to Analysis page
    with col_btn3:
        if st.button("➡️ About Us"):
            st.switch_page("pages/3 About Us.py")  # Navigate to About Us page