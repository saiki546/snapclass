import streamlit as st

def header_home():

    logo_url="https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;margin-bottom:30px;margin-top:30px">
        <img src="{logo_url}" style='height:100px';/>
        <h1 style="text-align:center; color:#E0E3FF">SNAP<br/>CLASS</h1>
    </div>
                """,unsafe_allow_html=True)
    
def header_dashboard():

    logo_url="https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="display:flex;align-items:left;justify-content:center;gap:10px;">
            <img src="{logo_url}" style="height:85px;">
            <div style="
                color:#5865F2;
                font-size:28px;
                font-weight:600;
                line-height:1.5;
                text-align:center;
                font-family:'Climate Crisis', sans-serif ;
            ">
                SNAP<br>CLASS
            </div>
        </div>
        """, unsafe_allow_html=True)
