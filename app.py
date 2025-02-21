import streamlit as st
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain, generate_questions_and_answers


# Function to handle user input
# def user_input(user_question):
#     response = st.session_state.conversation({"question": user_question})
#     st.session_state.chatHistory = response['chat_history']
    
#     for i, message in enumerate(st.session_state.chatHistory):
#         if i % 2 == 0:
#             st.write("User: ", message.content)
#         else:
#             st.write("Reply: ", message.content)

#new user input
def user_input(user_question):
    """Handles user input and determines if explanation + Q&A is needed."""
    if "explain" in user_question.lower() or "what is" in user_question.lower():
        explanation, qa_response = generate_questions_and_answers(user_question)

        # Explanation part
        st.write("Explanation")
        st.write(explanation)

        # question and answer part
        st.write("Related Questions & Answers")
        qa_lines = qa_response.split("\n")
        for line in qa_lines:
            st.write(line)
    else:
        response = st.session_state.conversation({"question": user_question})
        st.session_state.chatHistory = response['chat_history']
        for i, message in enumerate(st.session_state.chatHistory):
            role = "User: " if i % 2 == 0 else "Reply: "
            st.write(role, message.content)

def main():
    st.set_page_config(page_title="Information Retrieval App")

    st.markdown('<h1 style="font-family: serif; color:white; font-size: 20px;">Question Answer Chat-bot</h1>', unsafe_allow_html=True)

    # User Input
    user_question = st.text_input("How May I Help You?")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    if user_question:
        user_input(user_question)

    # sidebar part
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDFs", accept_multiple_files=True)
        
        if st.button("Submit & Process"):
            with st.spinner("Processing PDFs..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.conversation = get_conversational_chain(vector_store)

                st.success("Processing Complete!")

if __name__ == "__main__":
    main()
