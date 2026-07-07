import streamlit as st
from components.header import header_home

from ui.base_layout import style_base_layout,style_background_home,style_background_dashboard
def home_screen():
    
    header_home()

    style_base_layout()
    style_background_home()
    col1,col2=st.columns(2)

    with col1:
        if st.button("teacher portal"):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
    with col2:
        if st.button("student portal"):
            st.session_state['login_type'] = 'student'
            st.rerun()
