import streamlit as st
from PIL import Image
from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.header import header_dashboard
from src.pipelines.face_pipeline import predict_attendance,get_face_embeddings,train_classifier
from src.database.db import get_all_students,create_student,get_student_subjects,get_student_attendance,unenroll_student_to_subject
from src.pipelines.voice_pipeline import get_voice_embedding
import numpy as np
from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card
def student_dashboard():
    student_data=st.session_state.student_data
    student_id=student_data['student_id']
    col1,col2=st.columns(2,vertical_alignment='center',gap='xxlarge')
    with col1:
        header_dashboard()

    with col2:
        st.subheader(f"""Welcome,{student_data['name']}""")
        if st.button("Logout",type='secondary',key='loginbackbtn',shortcut="control+backspace"):
            st.session_state['is_logged_in']=False
            del st.session_state.student_data
            st.rerun()
    st.space()

    c1,c2=st.columns(2)
    with c1:
        st.header("Your Enrolled Subjects")

    with c2:
        if st.button('Enroll in Subject',type='primary',width='stretch'):
            enroll_dialog()

    st.divider()
    with st.spinner("Loading your enrolled subjects"):
        subjects=get_student_subjects(student_id)
        logs=get_student_attendance(student_id)

    stats_map={}
    for log in logs:
        sid=log['subject_id']
        if sid not in stats_map:
            stats_map[sid]={'total':0,'attended':0}

        stats_map[sid]['total']+=1

        if log.get('is_present'):
            stats_map[sid]['attended']+=1

    cols=st.columns(2)
    for i,sub_node in enumerate(subjects):
        sub=sub_node['subjects']
        sid=sub['subject_id']

        stats=stats_map.get(sid,{'total':0,'attended':0})
        def unenroll_btn():
            if st.button('UnEnroll from this Course',type='tertiary',width='stretch',icon=":material/delete_forever:"):
                unenroll_student_to_subject(student_id,sid)
                st.toast(f'Unenroll from {sub['name']} successfully')

        with cols[i%2]:
            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=[
                    ('🗓️','Total',stats['total']),
                    ('✅','Attended',stats['attended']),
                ],
                footer_callback=unenroll_btn
            )
def student_screen():
    style_background_dashboard()
    style_base_layout()

    if 'student_data' in st.session_state:
        student_dashboard()
        return 
    col1,col2=st.columns(2,vertical_alignment='center',gap='xxlarge')

    with col1:
        header_dashboard()

    with col2:
        if st.button("Go back to Home",type='secondary',key='loginbackbtn',shortcut="control+backspace"):
            st.session_state['login_type']=None
            st.rerun()


    st.header("Login Using Face ID",text_alignment='center')
    st.space()
    st.space()
    show_registration=False
    photo_source=st.camera_input("Position Your Face  In Center")
    if photo_source:
        img=np.array(Image.open(photo_source))

        with st.spinner("AI is Scanning.."):
            detected,all_ids,num_faces=predict_attendance(img)

            if num_faces==0:
                st.warning('Face not found!')

            elif num_faces>1:
                st.warning("Multiple Faces Found")

            else:
                if detected:
                    student_id=list(detected.keys())[0]
                    all_students=get_all_students()
                    student=next((s for s in all_students if s['student_id']==student_id),None)

                    if student:
                        st.session_state.is_logged_in=True
                        st.session_state.user_role='student'
                        st.session_state.student_data=student
                        st.toast(f"Welcome Back{student['name']}")
                        import time
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info('face not recognized! You might be a new student!')
                    show_registration=True

    if show_registration:
        with st.container(border=True):
            st.header("Register New Profile")
            new_name=st.text_input("Enter Tour Name",placeholder='E.g. sai kiran')

            st.subheader('optional:voice Enrollment')
            st.info("Enroll for voice only attendance")

            audio_data=None

            try:
                audio_data=st.audio_input('record a short phrase like i an present . My name is Sai Kiran')

            except Exception:
                st.error("Audio Data Failed")

            if st.button("create account",type='primary'):
                if new_name:
                    with st.spinner('Creating Profile..'):
                        img=np.array(Image.open(photo_source))
                        encodings=get_face_embeddings(img)
                        if encodings:
                            face_emb=encodings[0].tolist()

                            voice_emb=None
                            if audio_data:
                                voice_emb=get_voice_embedding(audio_data.read())

                            response_data=create_student(new_name,face_embedding=face_emb,voice_embedding=voice_emb )

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in=True
                                st.session_state.user_role='student'
                                st.session_state.student_data=response_data[0]
                                st.toast(f"profile created! Hi{new_name}!")
                                import time
                                time.sleep(1)
                                st.rerun()

                        else:
                            st.error("Couldn't capture your facial features for the registration")
                else:
                    st.error("Please Enter Your Name")    

