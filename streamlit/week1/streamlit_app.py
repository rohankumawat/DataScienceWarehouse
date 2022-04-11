import streamlit as st # import the library

# creating a header text for the app
st.header('st.button')

# printing alternative messages
if st.button('Say Hello'):      # st.button() accepts the label input argument of 'Say Hello' (The text that the button displays)
    st.write('Why Hello There') # Used to print text messages 
else:
    st.write('GoodBye')