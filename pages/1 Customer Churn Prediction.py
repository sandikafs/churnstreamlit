import pandas as pd
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Churn Predictor - E-Commerce Churn Prediction",
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

# Custom CSS for styling form layout
st.markdown("""
    <style>
        /* Global Background & Text */
        body, .main, .stApp {
            background-color: #ecf0f1 !important;  /* Light grey */
            color: white !important; /* Set all text to white */
        }
        /* Title container */
        .title-container {
            background-color: #0c1c10;
            padding: 20px;
            border-radius: 10px;
            text-align: left;
            color: white !important;
            font-size: 32px;
            font-weight: bold;   
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

        /* Form container */
        .form-container {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }

        /* Prediction bubble */
        .prediction-bubble {
            background-color: #4CAF50;
            color: white;
            padding: 15px;
            border-radius: 10px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            width: fit-content;
            margin: auto;
        }
    </style>
""", unsafe_allow_html=True)

# ================================
# **Title Section**
st.markdown('<div class="title-container">📊 E-Commerce Customer Churn Prediction</div>', unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_pipeline():
    with open('final_pipeline.pkl', 'rb') as f:
        pipeline = pickle.load(f)
    return pipeline

pipeline = load_pipeline()

# ================================
# **Customer Input Form (Inside the Main Page)**
# Add Explanation Bubble
st.markdown("""
    <div class="bubble">
        <h3>🔍 Understanding Customer Churn Prediction</h3>
        <p>Customer churn prediction helps businesses identify customers who are likely to stop using their services. 
        By analyzing past customer behavior, this model provides insights that enable businesses to take proactive measures 
        to improve retention and engagement.
        Please input the customer's feature on the sidebar.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""<div class="bubble">
                <h3>Customer Data</h3>
              </div>""", unsafe_allow_html=True)


with st.form("customer_form"):
    col1, col2 = st.columns(2)

    with col1:
        tenure = st.number_input("Tenure (Month)", min_value=0, max_value=61, step=1, value=1)
        warehouse_to_home = st.number_input("Warehouse to home (km)", min_value=5, max_value=127, step=1, value=6)
        marital_status = st.selectbox("Marital Status", ['Single', 'Divorced', 'Married'])
        number_of_address = st.number_input("Number of Address", min_value=1, max_value=10, step=1, value=3)
        number_of_device_registered = st.number_input("Number of Device Registered", min_value=1, max_value=6, step=1, value=4)
        order_count = st.number_input("Order Count", min_value=1, max_value=16, step=1, value=1)
        order_amount_hike = st.number_input("Order Amount Hike From Last Year", min_value=11, max_value=26, step=1, value=11)
        satisfaction_score = st.slider("Satisfaction Score", min_value=1, max_value=5, value=5)
        city_tier = st.radio("City Tier", ['1', '2', '3'])

    with col2:
        day_since_last_order = st.number_input("Day Since Last Order", min_value=0, max_value=31, step=1, value=1)
        cashback_amount = st.number_input("Cashback Amount ($)", min_value=0.0, max_value=324.99, step=1.0, value=120.00)
        complain = st.selectbox("Complain (0 = No Complain, 1 = Complain)", [0, 1])
        coupon_used = st.number_input("Coupons Used", min_value=0, max_value=16, step=1, value=0)
        prefered_order_cat = st.selectbox("Preferred Order Category", ['Laptop & Accessory', 'Mobile Phone', 'Others', 'Fashion', 'Grocery'])
        preferred_payment_mode = st.selectbox("Preferred Payment Mode", ['Debit Card', 'UPI', 'Credit Card', 'Cash on Delivery', 'E-wallet'])
        preferred_login_device = st.selectbox("Preferred Login Device", ['Mobile Phone', 'Computer'])
        hour_spent_on_app = st.slider("Hours Spent on App", min_value=1, max_value=5, value=1)
        gender = st.radio("Gender", ['Male', 'Female'])

    submit_button = st.form_submit_button("Predict")

st.markdown("""
<style>
/* 1. Green background for the form container */
[data-testid="stForm"] {
  background-color: #0c1c10;
}

/* 2. Grey text for labels, help text, and other text inside the form */
[data-testid="stForm"] label, 
[data-testid="stForm"] span, 
[data-testid="stForm"] .stMarkdown {
  color: #CCCCCC;
}

/* 3. Make input fields (text inputs, selects, textareas, etc.) black with grey text */
[data-testid="stForm"] input, 
[data-testid="stForm"] textarea, 
[data-testid="stForm"] select {
  background-color: #333333 !important;
  color: #CCCCCC !important;
}

/* (No explicit styling for the submit button, so it stays default) */
</style>
""", unsafe_allow_html=True)

# ================================
if submit_button:
    # Prepare input data as a DataFrame
    input_data = pd.DataFrame({
        "tenure": [tenure],
        "warehouse_to_home": [warehouse_to_home],
        "satisfaction_score": [satisfaction_score],
        "day_since_last_order": [day_since_last_order],
        "cashback_amount": [cashback_amount],
        "complain": [complain],
        "number_of_address": [number_of_address],
        "number_of_device_registered": [number_of_device_registered],
        "marital_status": [marital_status],
        "prefered_order_cat": [prefered_order_cat],
        "preferred_payment_mode": [preferred_payment_mode],
        "preferred_login_device": [preferred_login_device],
        "order_count": [order_count],
        "order_amount_hike_fromlast_year": [order_amount_hike],
        "coupon_used": [coupon_used],
        "hour_spend_on_app": [hour_spent_on_app],
        "city_tier": [city_tier],
        "gender": [gender]
    })

    # Force black text color
    styled_df = input_data.style.set_properties(**{
        'color': 'black'
    })



    # Make prediction
    churn_probability = pipeline.predict_proba(input_data)[0][1]

    # Display Results
    st.markdown(f"""
        <div class="prediction-bubble">
            {'🔴 High Churn Risk' if churn_probability > 0.5 else '🟢 Low Churn Risk'} <br>
            <b>Churn Probability:</b> {churn_probability:.2f}
        </div>
    """, unsafe_allow_html=True)
