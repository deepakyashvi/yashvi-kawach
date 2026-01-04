import streamlit as st

# यह कोड नीचे से 'Made with Streamlit' और ऊपर से प्रोफाइल का नाम छुपा देगा
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_contents=True)

# अब आपका अपना ब्रांडिंग
st.markdown("<h3 style='text-align: center; color: #FF4B4B;'>Yashvi Enterprise द्वारा सुरक्षित</h3>", unsafe_allow_html=True)
