import streamlit as st


# Page Config
st.set_page_config(
    page_title="My First App",
    page_icon="🌐",
    layout="centered"
)


# Title
st.title("Welcome to My Website 🌟")

# Subtitle / Description
st.write("This webpage is made using Python and Streamlit.")

st.markdown("---")


# Button Action
if st.button("Click Me"):
    st.success("Hello Div! 👋")


# Extra Section
st.markdown("### About This App")

st.info("""
This is a simple web app created using:

- Python 🐍
- Streamlit ☁️
- GitHub Actions 🚀
- Deployed on Streamlit Cloud
""")


# Footer
st.markdown("---")
st.caption("© 2026 | Created by Div")
