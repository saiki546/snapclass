import streamlit as st
from components.header import header_home

from ui.base_layout import style_base_layout,style_background_home,style_background_dashboard
def home_screen():
    style_base_layout()
    header_home()

    
    style_background_home()
    col1,col2=st.columns(2)

    with col1:
        st.header("I'm Student")
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png",width=145)
        if st.button("student portal",type="primary",icon=':material/arrow_outward:',icon_position='right'):
            st.session_state['login_type'] = 'student'
            st.rerun()


        
    with col2:
        st.header("I'm Teacher")
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png",width=145)
        st.markdown("<div style='height:25px;'></div>", unsafe_allow_html=True)
        if st.button("teacher portal",type="primary",icon=':material/arrow_outward:',icon_position='right'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
