import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Churn Analysis Dashboard - E-Commerce Churn Prediction",
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

# Custom CSS for styling
st.markdown("""
    <style>
        /* Global Background & Text */
        body, .main, .stApp {
            background-color: #ecf0f1 !important;  /* Light grey */
            color: white !important; /* Set all text to white */
        }
        /* Title container styling */
        .title-container {
            background-color: #0c1c10;  /* Darker Green */
            padding: 20px;
            border-radius: 10px;
            text-align: left;
            color: white !important; /* Ensure title text is white */
            font-size: 32px;
            font-weight: bold;    
        }

        /* Bubble caption styling */
        .caption-bubble {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #2c3e50;  /* Darker Grey */
            color: white;
            padding: 10px 20px;
            border-radius: 20px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            width: fit-content;
            margin: auto;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #0c1c10 !important;
            color: white !important;
            border-radius: 5px !important;
            padding: 8px 15px !important;
            font-weight: bold !important;
        }

        /* Aligning buttons */
        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# **Title Section** (Inside Title Container)
st.markdown('<div class="title-container">📊 E-Commerce Customer Churn Analysis</div>', unsafe_allow_html=True)

# List of image paths
image_paths = [
    r'C:\Users\Farhan\OneDrive\Pictures\Screenshots\Customer and Demographic Segment Dashboard.png',
    r'C:\Users\Farhan\OneDrive\Pictures\Screenshots\Screenshot 2025-02-26 212514.png',
    r'C:\Users\Farhan\OneDrive\Pictures\Screenshots\Software Interaction.png',
    r'C:\Users\Farhan\OneDrive\Pictures\Screenshots\Customer Satisfaction.png'
]

# Captions for each image
captions = [
    "📌 Customer and Demographic Segment Dashboard",
    "📌 Churn Rate Analysis",
    "📌 Software Interaction Metrics",
    "📌 Customer Satisfaction Overview"
]

# Initialize session state to keep track of the current image index
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# Function to go to the next image
def next_image():
    if st.session_state.current_index < len(image_paths) - 1:
        st.session_state.current_index += 1

# Function to go to the previous image
def prev_image():
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1

# **Caption inside a bubble**
st.markdown(f'<div class="caption-bubble">{captions[st.session_state.current_index]}</div>', unsafe_allow_html=True)

# Display the current image
current_image = Image.open(image_paths[st.session_state.current_index])
st.image(current_image)


# Add "Previous" and "Next" buttons in a row
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("⬅️ Previous"):
        prev_image()
with col3:
    if st.button("Next ➡️"):
        next_image()
