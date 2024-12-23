import streamlit as st

# Page title
st.set_page_config(page_title="CV Helper!", layout="centered")
st.markdown(
    """
    <style>
    a[href$="/"] {display: none;}

        a[href*="/home"]{
            display: none;
        }
        a[href*="/chatbot_page"]{
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def show():
    # Page title
    st.markdown(
        "<h1 style='text-align: center; color: black;'>CV Helper</h1>",
        unsafe_allow_html=True,
    )
    st.write("This is the welcome page for CV Helper. To use the Chatbot, please go to the Chatbot page")
    # st.image("static/images/face_det_image (2).jpg")
    if st.button("Start", use_container_width=True):
        st.switch_page("pages/chatbot_page.py")


show()