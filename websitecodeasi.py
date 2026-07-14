import streamlit as st

# Set the title of the website
st.title("My Python Web App")

# Create a text input field for the user
user_input = st.text_input("Enter some text here:")

# If the user has typed something, display it back to them
if user_input:
    st.write(f"You typed: {user_input}")
