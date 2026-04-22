import streamlit as st
from PIL import Image # Pillow (PIL) library is used for image processing

# Title
st.title("Welcome to Streamlit Library!!")

# Header and Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text - It shows how to display plain text in a Streamlit app.
st.text("This is a simple text message")

# Markdown - The ### creates a level 3 header, used for medium-sized headings in the app.
st.markdown("### This is a markdown ")

# Success, Info, Warning, Error and Exception
st.success("This is a success message")

st.info("This is an info message")

st.warning("This is a warning message")

st.error("This is an error message")

exp = ZeroDivisionError("Trying to divide by zero")
st.exception(exp)

# write - It can be used to display various types of content, including text, dataframes, and charts.
st.write("Text with write")
st.write(range(0,10))

# Display Images
img = Image.open("C:\\Users\\madha\\Downloads\\Streamlit.png") # Open the image by providing the file path.
st.image(img, width=200) # Display the image with specified width

# Checkbox - It creates a checkbox that users can interact with to show or hide content.
st.checkbox("Show/Hide Image") # Create a checkbox with a label and a unique key.
st.text("Showing the widget")

#Radio Button - It creates a set of radio buttons that allow users to select one option from a list.
status =st.radio("Select Gender:",['Male','Female'])
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

# Selection Box - It creates a dropdown selection box that allows users to choose one option from a list.
hobby = st.selectbox("Select a hobby",['Dancing','reading','sports','travelling'])
st.write("Your hobby is", hobby)

# Multiselect - It creates a multiselect box that allows users to select multiple options from a list.
hobbies = st.multiselect("Select your hobbies",['Dancing','reading','sports','travelling','cooking'])
st.write("You selected", len(hobbies), "hobbies")

#Button - It creates a button that users can click to trigger an action or event.
st.button("Click me")
if st.button("About"):
    st.text("Welcome to Streamlit Library") # When the "About" button is clicked, it displays the text "Welcome to Streamlit Library" in the app

# Text Input - It creates a text input field where users can enter text
name = st.text_input("Enter your name")
if st.button("Submit"):
    result = name.title()
    st.success(result)

# Slider - It creates a slider that allows users to select a value from a specified range.
level = st.slider("Choose a level",min_value =1,max_value=5)
st.write(f"Selected level: {level}")