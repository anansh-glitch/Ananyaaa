
import streamlit as st
import re

st.title("Password Strength Checker 🔐")

st.write("Enter a password to check its strength.")

password = st.text_input("Enter Password", type="password")

if password:
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add a number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    st.subheader(f"Password Score: {score}/5")

    st.progress(score / 5)

    if score <= 2:
        st.error("Password Strength: Weak")
    elif score <= 4:
        st.warning("Password Strength: Moderate")
    else:
        st.success("Password Strength: Strong")

    # Display suggestions
    st.subheader("Suggestions")

    if suggestions:
        for suggestion in suggestions:
            st.write("❌", suggestion)
    else:
        st.write("✅ All criteria satisfied!")

