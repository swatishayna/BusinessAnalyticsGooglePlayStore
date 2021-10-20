import streamlit as st
from PIL import Image


def writeup():

    st.title("Google Play Store Analytics\n\n")
    img1 = Image.open("resources/android.jpg")
    img2 = Image.open("resources/google-play-logo.jpg")

    left,right = st.columns(2)
    # display image using streamlit
    # width is used to set the width of an image
    left.image(img1, width=200)
    right.image(img2,width=200)

    st.subheader("Problem Statement:")

    st.text("""
    Technology is the increasing need nowadays and used everywhere. 
    One of the features of Technology is android which we all use in our daily life. 
    Android is a mobile operating system based on a modified version of the Linux kernel
    and other open source software, designed primarily for touchscreen mobile devices
    such as smartphones and tablets.Research needs to be done to figure out the hidden facts in the dataset. 
    Further model selection needs to be made to predict the ratings of the apps after the launch on Google App Store.""")