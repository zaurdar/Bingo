import streamlit as st
import cv2
img = cv2.imread("caca.jpeg")
st.image(img)