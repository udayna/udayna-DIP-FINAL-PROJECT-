from email.mime import image
from fileinput import filename
import imp
from secrets import choice
import streamlit as st
from PIL import Image


import style 

def main():

	menu = ["Image","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Image":
		st.subheader("Image")

def load_image(image_file):
	pic = Image.open(image_file)
	return pic

if choice == "Image":
    st.subheader("Image")
input_image = st.file_uploader("Upload Content Image", type=["png","jpg","jpeg"])

if input_image is not None:
    file_details = {"filename":input_image.name, "filetype":input_image.type,"filesize":input_image.size}
    st.write(file_details)
    st.image(load_image(input_image), width = 250)



style_name_1=st.sidebar.selectbox(
    'Select Style',
    ('candy', 'mosaic', 'udnie', 'rain_princess')
)



model= "saved_models/" + style_name_1 +".pth" 
 

output_image = "images/output-images/" + style_name_1 + ".jpg"


clicked=st.button("stylize")

if clicked:
    model=style.load_model(model)
    style.stylize(model,input_image,output_image)
    st.write("### OUTPUT Image:")
    image = Image.open(output_image)
    st.image(image, width=400)



