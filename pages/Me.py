import streamlit as st
import base64

# Set page configuration
st.set_page_config(
        page_title = "Fallou Fall Portfolio" ,
        page_icon = "🧪" ,
        )

# ----- Left menu -----
with st.sidebar :
    st.image("eae_img.png" , width = 200)
    st.header("Data Science 🧬 ")
    st.write("###")
    st.write(" Project Machine Learning - April 2024")
    st.write("**Author:**[Fallou Fall  ](https://github.com/FallouFall)")

# ----- Top title -----
st.write(
        f"""<div style="text-align: center;"><h2 style="text-align: center;">🧑🏽‍🔬 Hi! My name is Fallou Fall</h2></div>""" ,
        unsafe_allow_html = True)

# ----- Profile image file -----
profile_image_file_path = "./data/pp.jpg"

with open(profile_image_file_path , "rb") as img_file :
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="180" height="180" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""" , unsafe_allow_html = True)

current_role = "Master in Big & Data Analytics at EAE Business School Barcelona"

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""" , unsafe_allow_html = True)

st.write("##")

# Sidebar content

# ----- Left menu -----
with st.sidebar :
    st.image("eae_img.png" , width = 200)
    st.write(
            """I delved into the extensive dataset of car accidents in Barcelona, Catalonia. Through meticulous analysis, I uncovered temporal and spatial patterns, identified key factors contributing to accidents, and developed predictive models to forecast future occurrences. My findings provided valuable insights for policymakers and urban planners, guiding efforts to enhance traffic safety measures and mitigate risks. Ultimately, the journey exemplified the power of data science in driving positive societal change and fostering safer communities.""")
    st.write(
            "Data extracted from: https://opendata-ajuntament.barcelona.cat/data/es/dataset/accidents_causa_conductor_gu_bcn/resource/5a040155-38b3-4b19-a4b0-c84a0618d363/download/2023_accidents_causa_conductor_gu_bcn_.csv")

# ----- Title of the page -----

st.title("🚖 Catalunya Accidents 2023🚖")
st.divider()

# Contact information
st.title('Contact Page')
st.markdown(
        '''
        ## 🧑‍🎓 Data Science Web Application
        - **Tech Stack:** Python
        - **App URL:** [Data MLL App](https://bcn-driving.streamlit.app/)
        ## Projects
        - **H**
            - **GitHub:** [Machine-Learing-Barcelona-Accidents-2023](https://github.com/FallouFall/BarcelonaAccident.git)
            - **GitHub:** [Machine-Learing-Resto-Reviews](https://github.com/FallouFall/zomato-ml)
            - **GitHub:** [eae_ipld_project](https://github.com/FallouFall/eae_ipld_project)
            - **Tech Stack:** JavaFX/Springboot/Angular https://www.gnudem.com/
            - **GitHub:** [Hospital Management GitHub Repo](https://github.com/FallouFall/Hoggy_Web)
            - **App URL:** [Data Visualisation App](https://datavisualisation.streamlit.app/)
    
    
        - **t**
            - **Tech Stack:** JEE/Springboot/Continuous Integration
            - **GitHub:** [School Management GitHub Repo](https://github.com/FallouFall/GestionScolaire)
            - **GitHub (RMI Version):** [School Management with RMI GitHub Repo](https://github.com/FallouFall/ServeurGestionEtudiant)
            - **GitHub (Client Version):** [Client for School Management with RMI GitHub Repo](https://github.com/FallouFall/ClientGestionEtudiants)
            - **GitHub:** [Zomato Machine Learning](https://github.com/FallouFall/zomato-ml)
            - **GitHub:** [Barcelona Accident 2023 M-Learning](https://github.com/FallouFall/BarcelonaAccident.git)
        ---
    
        ## 📫 How to Reach Me:
        - **Email:** falloufalllive@gmail.com
        - **LinkedIn:** [Fallou Fall](https://www.linkedin.com/in/fallou-fall-047675173/)
        - **Tel:** Es (+34) 602552848) ,Us (+1) 769 274-0198, Sn (+221) 776880723
        ## 🏠 Location:
        - Barcelona: Lloret del Mar Barcelona
        '''
        )
