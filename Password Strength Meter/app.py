import re 
import random
import string
import streamlit as st

# list of commonly used passwords
COMMON_PASSWORDS = {"123456","qwerty","abc123","password123","password"}

# Function to Check Password Strength
def check_password_strength(password):
    score = 0
    message = []

    # Length Check
    if len(password) >=12 :
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        message.append("❌ Password should be at least 8 characters long.")  

    # Upper & Lowercase Check
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score += 1
    else:
        message.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d",password):
        score += 1
    else:
        message.append("❌ Add at least one number (0-9).")    

    # Special Character Check
    if re.search(r"[!@#$%^&*]",password):
        score += 1
    else:
        message.append("❌ Include at least one special character (!@#$%^&*).")

    # Common Password Check
    if password.lower() in COMMON_PASSWORDS:
        message.append("❌ This password is too common and easily guessable.")
        score = 0

    # Password Strength Rating
    if score >= 5:
        return "✅ Strong Password!",message
    elif score >= 3:
        return "⚠️ Moderate Password - Consider adding more security features.",message
    else:
        return "❌ Weak Password - Improve it using the suggestions.",message
    
# Function to Generate a Strong Password
def generate_password(length=12):
     characters = string.ascii_letters + string.digits + "!@#$%^&*"
     return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI for Password Meter
st.title("🔒 Password Strength Meter")
password = st.text_input("Enter your password:",type="password")

# Button to Check Password Strength
if st.button("Check Password Strength"):
    if password:
        result,suggestion = check_password_strength(password)
        st.write(result)
        for msg in suggestion:
            st.write(msg)
    else:
        st.write("❌ Please enter a password to check.")        

# Button to Generate a Strong Password
if st.button("Generate Strong Password"):
    strong_password = generate_password()
    st.write(f"🔑 Suggested Strong Password: `{strong_password}`")



