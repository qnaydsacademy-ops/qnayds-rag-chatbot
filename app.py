import streamlit as st

st.set_page_config(page_title="QNAYDS Hackers Academy")

st.title("QNAYDS Hackers Academy Bot")
st.markdown("Kerala's No.1 Ethical Hacking Institute - Manjeri")

query = st.text_input("Your Question:")

if query:
    st.success(f"Answer for '{query}': Please visit hackers-academy.qnayds.in for details. Our courses include Ethical Hacking, CTF Labs, Placement Support!")
