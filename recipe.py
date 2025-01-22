import streamlit as st
import os
import google.generativeai as genai
import time


os.environ['GOOGLE_API_KEY']='AIzaSyBmnMpaZIdCkdrPryfuNCqQSxh3HVhTd4k'
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model=genai.GenerativeModel("gemini-pro")

tab1, tab2 = st.tabs(["Intro", "Recipes"])



st.cache_data.clear()
# You can also use "with" notation:
with tab1:
     st.header("TasteBuddy🤤🍱🍗🍟")
     st.markdown("Developed by Soumendu")
     
     col1,col2=st.columns(2)
     col1,col2=st.columns(2,vertical_alignment="center")
     
     with col1:
         st.image("D:/project/images (14).jpeg",width=350)
     with col2:
       st.write("""Welcome to the Multi-Language Recipe Generator App!

Introducing an innovative app designed to make cooking easy and accessible for everyone, regardless of the language they speak! Whether you're a seasoned chef or a beginner in the kitchen, our app will assist you in preparing delicious dishes from across India in the language of your choice.

Simply enter the name of any dish, and our app will generate its detailed recipe in multiple Indian languages, making it perfect for users from all regions. No more struggling with language barriers while cooking your favorite dishes!""")


     st.subheader("""Features:

Easy-to-use interface: Just type in the dish name, and get the recipe instantly.
Recipes in various Indian languages: Choose from languages like Hindi, Bengali, Tamil, Telugu, Marathi, and more.
Step-by-step instructions: Get clear, concise instructions that help you cook with confidence.
Cook with ease, no matter where you are or what language you speak. Download the app now and start exploring the vast world of Indian cuisine in your preferred language!""")
     
     if  st.feedback(options="stars"):
       st.toast("feedback submitted...")

with tab2:
     col3,col4=st.columns(2)


     col3,col4=st.columns(2,vertical_alignment="bottom")


     with col3:
       language=st.selectbox("Select Language",["English","Bengali","Hindi","Tamil","Telugu","Odia","Marathi","punjabi"])

       
     user_input=st.text_input("Enter your recipe")
     if st.button("Give Recipe"):
          prompt=f"""
       you are a fantastic chef! Please provide the ingredients and cooking instructions for the following dishes in this {language}language with correctly.
       ```
       {user_input}
        ```
        """
          
          if(user_input==''):
                 st.error("Please enter a dish name to get the recipe.")
          else: 
                with st.spinner(text="In progress"):
            
                 response=model.generate_content(prompt)
                 time.sleep(1)  # Indent properly
                 st.success("{}.".format(response.text))
                 if st.button("Clear"):
                     st.cache_data.clear()
          