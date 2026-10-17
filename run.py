# streamlit ---it is a open source python library that lets a create a beautfull web app without using HTML,CSS,JS.
print("Hi")

import streamlit as st
st.title("💥Welcome TO my First Website🚀")
st.subheader("Built with python & streamlit")
st.write("Hello everyone! this is a my first website.")

st.divider()

st.sidebar.title("About me")
st.sidebar.write("Name : Aadarsh Gupta")
st.sidebar.write("Roll : Beginer python developer")
st.sidebar.write("Goal : Build project for Github & linkdin")

st.header("✨Interactive  !! Greating Form")

user_name=st.text_input("Enter your name :")

fav_field=st.selectbox("select your fav. domain/tech :",
                       
["python","AI & ML","webdevelopment","cyberSecurity","contentCrator"]

)

if st.button("Generate Welcome Card"):
  if user_name:
    st.success(f"Hello {user_name} ! welcome Aboard 🎉")
    st.info(f"It's awesome that you are interested in **{fav_field}**!")

    st.balloons()
  else:
    st.warning("Please enter your name first")

st.divider()


st.caption("Made with ❤️ using Python & Streamlit | Shared on GitHub")