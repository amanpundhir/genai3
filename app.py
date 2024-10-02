import streamlit as st
import google.generativeai as genai
import os

# Initialize the API with your API Key
API_KEY = "AIzaSyCKMpA51iLjyHDST_d0IQfeolnvxcAHDJk"
genai.configure(api_key=API_KEY)

# Initialize the GenerativeModel with the correct model name
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to generate AI response
def generate_ai_response(student_input, conversation_history):
    prompt = f"""
    You are a friendly and helpful AI assistant for students of all levels.
    The student has asked the following question: {student_input}.
    
    Provide a clear, direct, and simple answer to this question. Avoid using any formatting like bold or italics (such as ** or *). 
    The answer should be easy to understand and focus on explaining the concept in a concise way.
    
    Remember the previous parts of the conversation and use this context to provide relevant and helpful answers.

    Here is the current conversation:
    {conversation_history}
    
    The student has now asked the following question: {student_input}.
    
    Please provide a clear, direct, and simple answer based on the previous context, without asking for clarification unless absolutely necessary.
    """
    
    # Generate response from the model based on the student's input
    response = model.generate_content(prompt)
    
    return response.text

# Streamlit interface
def main():
    st.title("AI-Powered Learning Assistant")

    # Initialize session state for conversation history
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = ""

    # Display input box for student query
    student_input = st.text_input("What would you like to learn or ask today?")

    # Use columns to arrange the buttons side by side
    col1, col2 = st.columns([1, 11])  # Adjust the size as necessary

    with col1:
        # Submit button
        if st.button("Ask"):
            if student_input:
                # Append the student's input to the conversation history
                st.session_state.conversation_history += f"Student: {student_input}\n"

                # Generate AI response
                assistant_response = generate_ai_response(student_input, st.session_state.conversation_history)

                # Append the assistant's response to the conversation history
                st.session_state.conversation_history += f"Assistant: {assistant_response}\n"

    with col2:
        # Clear History button
        if st.button("Clear History"):
            st.session_state.conversation_history = ""  # Reset conversation history

    # Display conversation history with a scrollable box
    if st.session_state.conversation_history:
        st.text_area("Conversation History", value=st.session_state.conversation_history, height=300)

if __name__ == "__main__":
    main()
