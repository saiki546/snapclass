import streamlit as st
import time
from PIL import Image
from src.database.db import create_attendance
from src.database.config import supabase
def show_attendance_results(df,logs):
    st.write('please review attendance before confirming.')
    st.dataframe(df,hide_index=True,width='stretch')
    c1,c2=st.columns(2)
    with c1:
       
        if st.button('Discard',width='stretch'):
           st.session_state.voice_attendance_results=None
           st.session_state.attendance_images=[]
           st.rerun()
    with c2:
        if st.button('Confirm & save',width='stretch',type='primary'):
    
            try:
                create_attendance(logs)
                st.toast("Attendance Taken")
                st.session_state.attendance_images=[]
                st.session_state.voice_attendance_results=None
                st.rerun()
            except Exception as e:
                st.error("Sync Failed")
@st.dialog('Attendance Reports')
def attendance_result_dialog(df,logs):

    show_attendance_results(df,logs)
   
        
    