import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv", sep=";")
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    Hi, I am Ardit! I am a Python programmer, teacher, and founder of PythonHow. I graduated in 2013 with a Master of Science in Geospatial Technologies from the University of Muenster in Germany with a focus on using Python for remote sensing.
I have worked with companies from various countries, such as the Center for Conservation Geography, to map and understand Australian ecosystems, image processing with the Swiss in-Terra, and performing data mining to gain business insights with the Australian Rapid Intelligence.
    """
    st.info(content)

content2 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Aliquet bibendum enim facilisis gravida neque convallis a cras. Morbi tincidunt ornare massa eget. Semper viverra nam libero justo. Et netus et malesuada fames ac. Orci nulla pellentesque dignissim enim sit amet venenatis urna cursus. Feugiat nibh sed pulvinar proin gravida hendrerit lectus a. Lorem donec massa sapien faucibus. Consectetur lorem donec massa sapien. Integer eget aliquet nibh praesent tristique. Orci phasellus egestas tellus rutrum tellus pellentesque. Scelerisque felis imperdiet proin fermentum leo vel orci porta. Id nibh tortor id aliquet lectus proin nibh nisl. Amet dictum sit amet justo donec enim. Pulvinar sapien et ligula ullamcorper malesuada proin libero. Quis ipsum suspendisse ultrices gravida dictum fusce ut placerat. Sed nisi lacus sed viverra tellus in.
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
