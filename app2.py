import re
import streamlit as st

st.set_page_config(page_title="Password Strength Meter by Abdul Rehman", page_icon="🔑", layout="centered")

# Custom CSS
st.markdown(
    """
    <style>
        .main {text-align: center;}
        .stTextInput {width: 60% !important; margin: auto;}
        .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
        .stButton button:hover {background-color: #45a049;}
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and description
st.title("🔐 Password Strength Generator")
st.write("Enter your password to check its security level. 🔎")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1  # Increment score by 1
    else:
        feedback.append(" ❌ Password should have at least 8 characters")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append(" ❌ Password should have both uppercase and lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append(" ❌ Password should have at least one digit")

    # Check special characters
    if re.search(r"[!@$%^&*]", password):
        score += 1
    else:
        feedback.append(" ❌ Password should have at least one special character")

    # Display password strength results
    if score == 4:
        feedback.append(" ✅ Your password is strong")
    elif score >= 3:
        feedback.append(" ⚠️ Your password is medium")
    else:
        feedback.append(" ❗️ Your password is weak")

    return feedback

password = st.text_input("Enter your password", type="password", help="Ensure your password is strong 🔐")

# Button functionality
if st.button("Check"):
    if password:
        feedback_messages = check_password_strength(password)
        with st.expander("Improve your password"):
            for message in feedback_messages:
                st.write(message)
    else:
        st.warning("Please enter a password first.")



                         

             
        
                 





