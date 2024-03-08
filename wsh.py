import streamlit as st

st.set_page_config(
    page_title="GREAT Internship",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="star"
)


def main():
    st.title("WALL OF WISHES")

    # Add a text box
    user_input = st.text_area("Enter some text:", "")

    # Display the entered text
    st.write("You entered:", user_input)

if __name__ == "__main__":
    main()