import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="About Us - E-Commerce Churn Prediction",
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

add_sidebar_header()

# Inject CSS to style bubbles and containers
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
            border-radius: 10px;
            text-align: left;
            font-size: 32px;
            margin-bottom: 20px;
            font-weight: bold;
            color: white !important;
        }
    .bubble {
        background-color: #4CAF50;
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        }
    /* Center Images */
        .image-container {
            text-align: center;
            margin-bottom: 15px;
        }
    
    </style>
""", unsafe_allow_html=True)

# "About Us" Section
st.markdown('<div class="title-container">👥 About Us</div>', unsafe_allow_html=True)

# Create two columns: One for project background, one for team members
col1, colspace, col2 = st.columns([1.7, 0.2, 1.8])

# "How it Works" Section
with col1:
    st.markdown("""
        <div class="bubble">
            <p>Thanks for accessing this website! 🚀</p>
            <p>
                Developed as the final project for the <strong>Job Connector Data Science Program at Purwadhika Jakarta</strong>,
                this app combines data science and business insights to help organizations analyze and predict customer churn effectively.
            </p>
        </div>
    """, unsafe_allow_html=True)

# "Team Members" Section
with col2:
    st.markdown("""
        <div class="bubble">
            <p>This Streamlit app was built by our team of three:</p>
        </div>
    """, unsafe_allow_html=True)

    # Create columns for team members
    team_col1, _, team_col2, _, team_col3 = st.columns([1, 0.3, 1, 0.3, 1])

    with team_col1:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image("https://media.licdn.com/dms/image/v2/D5635AQGT7OUbkN5kMw/profile-framedphoto-shrink_200_200/profile-framedphoto-shrink_200_200/0/1733384925722?e=1740913200&v=beta&t=G9ux836FiH9YWj9j7n1CmUPSehkW1rc2SRLAxxQ6evE", width=150)
        st.markdown('<div class="container"><div class="bubble"><a href="https://www.linkedin.com/in/nur-faaizah-faradhilah-ridwan/" target="_blank"><strong>Faaizah</strong></a></div></div>', unsafe_allow_html=True)

    with team_col2:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image("https://media.licdn.com/dms/image/v2/C4E03AQHu8ykXFBSDUQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1594538102959?e=1746057600&v=beta&t=zQDdFLdow4cadMCkdQqoUjmVgqUzSxJHVNqcONJ5jdg", width=150)
        st.markdown('<div class="container"><div class="bubble"><a href="https://www.linkedin.com/in/farhansandika/" target="_blank"><strong>Farhan</strong></a></div></div>', unsafe_allow_html=True)

    with team_col3:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image("https://media.licdn.com/dms/image/v2/D5603AQFD2truLLLfOA/profile-displayphoto-shrink_200_200/B56ZPKlPwzGwAY-/0/1734270582965?e=1746057600&v=beta&t=1KQEguwLGsnBKUcC_p8oOY6KzNj04jPB3JZ58oUZ1h8", width=150)
        st.markdown('<div class="container"><div class="bubble"><a href="https://www.linkedin.com/in/rina-adibah/" target="_blank"><strong>Rina</strong></a></div></div>', unsafe_allow_html=True)
