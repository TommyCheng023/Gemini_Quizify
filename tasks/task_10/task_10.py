import streamlit as st
import os
import sys
import json
sys.path.append(os.path.abspath('../../'))
from tasks.task_3.task_3 import DocumentProcessor
from tasks.task_4.task_4 import EmbeddingClient
from tasks.task_5.task_5 import ChromaCollectionCreator
from tasks.task_8.task_8 import QuizGenerator
from tasks.task_9.task_9 import QuizManager

if __name__ == "__main__":
    
    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "gemini-quizify-417301",
        "location": "us-central1"
    }
    screen = st.empty()
    
    # Add Session State
    if 'question_bank' not in st.session_state or len(st.session_state['question_bank']) == 0:
        # Initialize the question bank list in st.session_state
        st.session_state['question_bank'] = []
    
        with screen.container():
            st.header("Quiz Builder")
            
            # Create a new st.form flow control for Data Ingestion
            with st.form("Load Data to Chroma"):
                st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
                
                processor = DocumentProcessor()
                processor.ingest_documents()
            
                embed_client = EmbeddingClient(**embed_config) 
            
                chroma_creator = ChromaCollectionCreator(processor, embed_client)

                # Set topic input and number of questions
                topic_input = st.text_input(label="Topic for Generative Quiz", placeholder="Enter the topic of the document.")
                num_questions = st.slider(label="Number of Questions", min_value=1, max_value=10, value=1)
                    
                submitted = st.form_submit_button("Submit")
                
                if submitted:
                    chroma_creator.create_chroma_collection()
                        
                    if len(processor.pages) > 0:
                        st.write(f"Generating {num_questions} questions for topic: {topic_input}")

                    generator = QuizGenerator(topic_input, num_questions, chroma_creator)
                    question_bank = generator.generate_quiz()
                    # Initialization
                    st.session_state['question_bank'] = question_bank
                    st.session_state['display_quiz'] = True
                    st.session_state['question_index'] = 0

    elif st.session_state['display_quiz']:
        
        st.empty()
        with st.container():
            st.header("Generated Quiz: ")
            quiz_manager = QuizManager(st.session_state['question_bank'])
            
            # Format the question and display it
            with st.form("MCQ"):
                index_question = quiz_manager.get_question_at_index(0)
                
                # Unpack choices for radio button
                choices = []
                for choice in index_question['choices']:
                    key = choice['key']
                    value = choice['value']
                    choices.append(f"{key}) {value}")
                
                # Display the Question
                st.write(f"{st.session_state['question_index'] + 1}. {index_question['question']}")
                answer = st.radio(
                    "Choose an answer",
                    choices,
                    index = None
                )
                
                answer_choice = st.form_submit_button("Submit")

                # New feature: proceed & go back
                st.form_submit_button("Next Question, on_click=lambda: quiz_manager.next_question_index(direction=1)")
                st.form_submit_button("Previous Question, on_click=lambda: quiz_manager.next_question_index(direction=-1)")

                
                if answer_choice and answer is not None:
                    correct_answer_key = index_question['answer']
                    if answer.startswith(correct_answer_key):
                        st.success("Correct!")
                    else:
                        st.error("Incorrect!")
                    st.write(f"Explanation: {index_question['explanation']}")