# Project : Growth Mindset Project 

import streamlit as st 

st.title ("Growth Mindset Challenge: Web App with Streamlit")
st.header ("✈️ Welcome to Your Growth Journey !")
st.write("Embrace challenges,learn from mistake , and unlock your full potential. This AI-powered app helps you  build a growth mindset with reflection,challenges,and achievements!⭐")
st.header ("💡 Today's Growth Mindset Quote ")
st.write ("Success is not final, failure is not fatal:its is the courage to continue that counts.")

st.header ("🔧What's your challenge today ?  ")
user_input = st.text_input ("Describe a challenge you,re facing ")


#condition 
if user_input:
    st.success(f"💪You're facing: {user_input}. keep pushing forward towards your goal 🌕 ")
else: 
    st.warning ("Tell us about your challenge to get started! ")

#
st.header ("Reflect on your learning ")
reflection = st.text_area ("Write your reflection here:")

if reflection:
    st.success (f"✨ Great Insight! Your reflection :{reflection}")
else:
    st.info("Reflecting on past experience help you grow!Share your difficulties")

#achievenment 
st.header ("🏆 Celebrate Your Wins !")
achievenment = st.text_input("Share something you've recently accomplished:")


if achievenment :
    st.success(f"💫Amazing ! You Achieved : {achievenment}")
else:
    st.info("Big or Small , every achievenment counts! Share one now 🥰")


#footer 
st.write ("- - -")
st.write("🛩️ Keep beleveing in yourself . Growth is a jorney, not a destination!🌚 ")
st.write("🧸**Created By Shifa Nawed ** ")