import streamlit as st

# Add title to webpage
st.title("Streamlit Demo")

# Add Header
st.header("Heading of Streamlits")

# Add sub header
st.subheader("Sub Heading")

# Add text
st.text("This is an example test")

# Add a success messsage
st.success("Success")

# Add a warning messsage
st.warning("Warning")

# Add a info messsage
st.info("Info")

# Add an error messsage
st.error("Error")

# Add checkbox
if st.checkbox('Select/Unselect'):
    st.text("Text Selected")
else:
    st.text("User not selected")
    
# Get radio buttons
state = st.radio("What is your fav color?",("Red","Green","Yellow"))

if state == 'Green':
    st.success("You have chosen Green")
else:
    st.info("You have chosen another color")

# Selection box    
occupation = st.selectbox("What do you do?",['Student','Engineer','Unemployed'])

st.info(f"Selected option is {occupation}")

# Button 
button=st.button("Submit")

if button:
    st.info('Submit button clicked')
else:
    st.info("Submit button not clicked")
    
st.sidebar.header("Heading of sidebar")
st.sidebar.text("Created by Nishchal")