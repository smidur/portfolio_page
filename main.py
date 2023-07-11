import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Aliquet bibendum enim facilisis gravida neque convallis a cras. Morbi tincidunt ornare massa eget. Semper viverra nam libero justo. Et netus et malesuada fames ac. Orci nulla pellentesque dignissim enim sit amet venenatis urna cursus. Feugiat nibh sed pulvinar proin gravida hendrerit lectus a. Lorem donec massa sapien faucibus. Consectetur lorem donec massa sapien. Integer eget aliquet nibh praesent tristique. Orci phasellus egestas tellus rutrum tellus pellentesque. Scelerisque felis imperdiet proin fermentum leo vel orci porta. Id nibh tortor id aliquet lectus proin nibh nisl. Amet dictum sit amet justo donec enim. Pulvinar sapien et ligula ullamcorper malesuada proin libero. Quis ipsum suspendisse ultrices gravida dictum fusce ut placerat. Sed nisi lacus sed viverra tellus in.
    """
    st.info(content)
