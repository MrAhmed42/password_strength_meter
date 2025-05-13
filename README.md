# 🔒 Password Strength Meter

A simple and interactive **Password Strength Meter** built using **Python** and **Streamlit**. This tool helps users evaluate the strength of their passwords and suggests improvements for better security. It also includes a feature to generate strong passwords.

🔗 **Live App**: [Click here to try it out](https://password-strength-meter-c5y47appdkzafn67shxapsp.streamlit.app/)  
💻 **Tech Used**: Python, Streamlit, Regular Expressions

## 🚀 Features

- Check if a password is:
  - Long enough (minimum 8 characters, ideally 12+)
  - Includes uppercase and lowercase letters
  - Includes numbers
  - Includes special characters (!@#$%^&*)
  - Is not a common/weak password
- Generate strong passwords with one click

## 🧠 How It Works

The password is evaluated on 5 key criteria. Each satisfied condition increases the strength score:
- ✅ Length
- ✅ Letter case variety
- ✅ Numeric inclusion
- ✅ Special character inclusion
- ✅ Avoiding common weak passwords

The app returns:
- `Strong Password`
- `Moderate Password`
- `Weak Password` with helpful suggestions

## 🛠️ How to Run Locally

```bash
pip install streamlit
streamlit run your_script_name.py
