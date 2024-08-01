import streamlit as st
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain


# bg-image


def user_input(user_question):
    # initializing the session and storing the question
    response = st.session_state.conversation({"question": user_question})
    # storing the answer in chat history
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.write("User: ", message.content)
        else:
            st.write("Reply: ", message.content)


def main():
    # setting the title of the website
    st.set_page_config("Information Retrieval-APP")

    # Title
    original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;">Information-Retrieval-APP </h1>'
    st.markdown(original_title, unsafe_allow_html=True)

    # setting the header of the app
    # st.header("Information-Retrieval-APP")

    # Set the background image
    background_image = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
        background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
        background-position: center;  
        background-repeat: no-repeat;
    }
    </style>
    """
    st.markdown(background_image, unsafe_allow_html=True)

    # input-style
    input_style = """
    <style>
    input[type="text"] {
        background-color: transparent;
        color: #a19eae;  // This changes the text color inside the input box
    }
    div[data-baseweb="base-input"] {
        background-color: transparent !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: transparent !important;
    }
    </style>
    """
    st.markdown(input_style, unsafe_allow_html=True)

    # user-input
    user_question = st.text_input("How May I Help You?")

    # logic to chat with the bot
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    if user_question:
        user_input(user_question)

    # creating a sidebar
    with st.sidebar:
        st.title("Menu:")
        # window to upload a pdf file
        pdf_docs = st.file_uploader(
            "Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        # button to submit
        if st.button("Submit & Process"):
            # visual animation of a proccessing
            with st.spinner("PDF is being processed..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                # store this conversation as history in a newly created session
                st.session_state.conversation = get_conversational_chain(
                    vector_store)

                st.success("Done")


if __name__ == "__main__":
    main()
