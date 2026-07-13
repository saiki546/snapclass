import streamlit as st

from src.database.db import create_subject

@st.dialog('Create New Subject')
def create_Subject_dialog(teacher_id):
    st.write('Enter The Details Of New Subject')
    sub_id=st.text_input('subject code',placeholder='CS101')
    sub_name=st.text_input('Subject_Name',placeholder='Introduction To Machine Learning')
    sub_section=st.text_input('Section',placeholder='A')

    if st.button('Create Subject Now',type='primary',width='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id,sub_name,sub_section,teacher_id)
                st.toast('Subject Created Successfully!!')
                st.rerun()
            except Exception as e:
                st.error(f"Error:{str(e)}")

        else:
            st.warning("Please fill all the fields")
