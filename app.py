import streamlit as st
import random
from chatbot import Chatbot
from nlp_processor import NLPProcessor
from quiz_manager import QuizManager


def main():
    st.title("🤖 Jokes & Trivia Chatbot")

    # Initialize our components
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = Chatbot()
    if 'nlp_processor' not in st.session_state:
        st.session_state.nlp_processor = NLPProcessor()
    if 'quiz_manager' not in st.session_state:
        st.session_state.quiz_manager = QuizManager()
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'quiz_active' not in st.session_state:
        st.session_state.quiz_active = False
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("What's on your mind?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Process user input
        intent = st.session_state.nlp_processor.get_intent(prompt.lower())

        with st.chat_message("assistant"):
            response = ""
            if intent == "joke":
                response = st.session_state.chatbot.tell_joke()
                st.write(response)

            elif intent == "trivia":
                topic = st.session_state.nlp_processor.extract_topic(prompt)
                if topic:
                    response = st.session_state.chatbot.tell_trivia(topic)
                    st.write(response)
                else:
                    response = "Please specify a topic for the trivia!"
                    st.write(response)

            elif intent == "quiz":
                topic = st.session_state.nlp_processor.extract_topic(prompt)
                if topic:
                    st.session_state.quiz_active = True
                    st.session_state.current_question = 0
                    st.session_state.quiz_score = 0
                    quiz = st.session_state.quiz_manager.create_quiz(topic)
                    response = f"Let's start a quiz about {topic}!\n{quiz[0]['question']}\n\n"
                    for i, option in enumerate(quiz[0]['options']):
                        response += f"{option}\n"
                    st.write(response)

                    # Add answer selection
                    user_answer = st.selectbox("Select your answer:", ["A", "B", "C", "D"])
                    if st.button("Submit Answer"):
                        if user_answer == quiz[0]['correct_answer']:
                            st.success("Correct!")
                            st.session_state.quiz_score += 1
                        else:
                            st.error(f"Wrong! The correct answer was {quiz[0]['correct_answer']}")
                else:
                    response = "Please specify a topic for the quiz!"
                    st.write(response)

            else:
                response = "I can tell jokes, share trivia, or create quizzes. Just let me know what you'd like!"
                st.write(response)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()