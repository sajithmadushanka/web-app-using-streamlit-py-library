import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
st.set_page_config(page_title="MY web", page_icon=":waving_hand:", layout="wide")
##-------------

def load_lotter(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("styles/main.css")


lottie_coding = "https://lottie.host/e3ebc5b1-4161-4ff7-9f15-55ac2e9b116c/Ci42mvlGBi.json"
img_contact_form =Image.open("images/cover.png")
img_lottie_animation =Image.open("images/download.jpg")
lottie_email = "https://lottie.host/565f08fe-cbc4-48e9-a7e9-375e8a9555f1/ySNAirCGUj.json"

# ---header section
st.subheader("Hi! I'm Sajith :wave:")
st.title("Web and Mobile developer From Sri Lanka")
st.write("Programming is my unwavering passion, driving my every endeavor in the world of technology.")
st.write("[Leeran more > ](https://python.org)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what I do")
        st.write("##")
        st.write(
            '''My passion for programming runs deep, shaping not 
            only my career but also my outlook on life. Each line of code 
            I write is a canvas for my creativity, a puzzle waiting to be solved, 
            and a gateway to innovation. Beyond the boundaries of work, 
            I find myself engrossed in the world of programming, constantly 
            exploring new languages, frameworks, and technologies. Whether 
            it's a humble script or a complex application, the act of coding is akin 
            to artistry, where I craft solutions to real-world challenges. To me, 
            being passionate about programming isn't just a choice; it's a commitment 
            to excellence, a relentless drive to learn, adapt, 
            and innovate in this ever-evolving field.'''
        )
        st.write("[linkedin](https://youtube.com)")

        with right_column:
            st_lottie(lottie_coding,height=300, key="coding")
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
        
    with text_column:
        st.subheader("ecommernce webiste")
        st.write('''
                Lorem Ipsum is simply dummy text of the printing and typesetting 
            industry. Lorem Ipsum has been the industry's standard dummy text 
            ever since the 1500s, when an unknown printer took a galley of type 
            and scrambled it to make a type specimen book. It has survived not 
            only five centuries, but also the leap into electronic typesetting,
            remaining essentially unchanged. It was popularised in the 1960s 
                ''')
        st.markdown('[view more](http://youtube.com)')
    with image_column:
        st.image(img_lottie_animation)

    with text_column:
        st.subheader("Block Chain Mobile appilcation")
        st.write('''
                Lorem Ipsum is simply dummy text of the printing and typesetting 
            industry. Lorem Ipsum has been the industry's standard dummy text 
            ever since the 1500s, when an unknown printer took a galley of type 
            and scrambled it to make a type specimen book. It has survived not 
            only five centuries, but also the leap into electronic typesetting,
            remaining essentially unchanged. It was popularised in the 1960s 
                ''')
        st.markdown('[view more](http://youtube.com)')

#-- contact form
with st.container():
    st.write("---")
    st.header("Get in touvh with me!")
    st.write("##")
    contact_form ='''
     <form action="https://formsubmit.co/madhusa720@gmail.com" method="POST">
     <input type="text" name="name" required placeholder = "enter name" class="name"> <br>
     <input type="email" name="email" required placeholder = "enter email"> <br>
     <textarea name = "message" placeholder ="enter your message here"></textarea> <br>  
     <button type="submit">Send</button>
</form>
    '''
left_column,right_column =st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st_lottie(lottie_email,height=300, key="cording")