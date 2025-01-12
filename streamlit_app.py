# streamlit_app.py

# Import necessary libraries

import streamlit as st
import os
import json
from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from pydantic import BaseModel, Field
from typing import List
# **Add this block to securely set the API key**

# Option 1: Use python-dotenv to load environment variables from a .env file
from dotenv import load_dotenv
load_dotenv()  # Loads variables from .env into environment variables

# Get the API key from environment variables
# Load the API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY is not set. Please set it in your environment variables.")
    st.stop()
else:
    # Optionally check the length of the API key
    st.write("API key detected.")

# Ensure the API key is set for `litellm`
os.environ["GEMINI_API_KEY"] = api_key

# Initialize the LLM with the Gemini model
gemini_llm = LLM(model="gemini/gemini-1.5-pro", temperature=0)

# Define the knowledge base
educational_content = """
This knowledge base contains information on programming concepts, data analytics, and language learning materials.
"""

tutor_knowledge = StringKnowledgeSource(
    content=educational_content
)

# Output directory
output_dir = "./educational-tutor-output"
os.makedirs(output_dir, exist_ok=True)

# **Include Data Model Definitions**

# Quiz data models
class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    correct_answer: int  # Index of the correct answer in options

class Quiz(BaseModel):
    topic: str
    questions: List[QuizQuestion]

# Flashcard data models
class Flashcard(BaseModel):
    front: str = Field(..., title="Term or question")
    back: str = Field(..., title="Definition or answer")

class Flashcards(BaseModel):
    topic: str
    cards: List[Flashcard]

# Grammar correction feedback data model
class CorrectionFeedback(BaseModel):
    original_text: str
    corrected_text: str
    feedback: str

# Project guidance data model
class ProjectGuidance(BaseModel):
    project_topic: str
    resources: List[str]
    steps: List[str]
    tips: List[str]

# **Define Agents**

quiz_generator_agent = Agent(
    role="Quiz Generator Agent",
    goal="Create interactive quizzes on a given topic to help learners test their knowledge.",
    backstory="The agent generates quizzes that are engaging and educational.",
    llm=gemini_llm,
    verbose=True,
)

flashcards_creator_agent = Agent(
    role="Flashcards Creator Agent",
    goal="Create flashcards to help learners memorize key concepts.",
    backstory="The agent focuses on summarizing information into digestible flashcards.",
    llm=gemini_llm,
    verbose=True,
)

grammar_correction_agent = Agent(
    role="Grammar Correction Agent",
    goal="Provide real-time grammar correction and feedback for learners.",
    backstory="The agent helps learners improve their language skills by correcting mistakes.",
    llm=gemini_llm,
    verbose=True,
)

project_guidance_agent = Agent(
    role="Project Guidance Agent",
    goal="Provide step-by-step guidance on projects in topics like Python, SQL, or Tableau.",
    backstory="The agent assists learners in completing projects by breaking down tasks.",
    llm=gemini_llm,
    verbose=True,
)

# **Define Tasks**

quiz_generation_task = Task(
    description="Generate a quiz with multiple-choice questions on the topic '{topic}'. Each question should have 4 options.",
    expected_output="A JSON object containing the quiz questions and answers.",
    output_json=Quiz,
    output_file=os.path.join(output_dir, "quiz.json"),
    agent=quiz_generator_agent
)

flashcards_creation_task = Task(
    description="Create a set of flashcards for the topic '{topic}'. Each flashcard should focus on a key concept or term.",
    expected_output="A JSON object containing the flashcards.",
    output_json=Flashcards,
    output_file=os.path.join(output_dir, "flashcards.json"),
    agent=flashcards_creator_agent
)

grammar_correction_task = Task(
    description="Correct the grammar of the following text and provide feedback.\n\nText: '{text}'",
    expected_output="A JSON object containing the corrected text and feedback.",
    output_json=CorrectionFeedback,
    output_file=os.path.join(output_dir, "grammar_correction.json"),
    agent=grammar_correction_agent
)

project_guidance_task = Task(
    description="Provide guidance for a project on '{project_topic}'. Include resources, steps, and tips.",
    expected_output="A JSON object containing the project guidance.",
    output_json=ProjectGuidance,
    output_file=os.path.join(output_dir, "project_guidance.json"),
    agent=project_guidance_agent
)

# Create the Crew
educational_tutor_crew = Crew(
    agents=[
        quiz_generator_agent,
        flashcards_creator_agent,
        grammar_correction_agent,
        project_guidance_agent,
    ],
    tasks=[
        quiz_generation_task,
        flashcards_creation_task,
        grammar_correction_task,
        project_guidance_task,
    ],
    process=Process.sequential,
    knowledge_sources=[tutor_knowledge]
)

# Streamlit App Interface
def main():
    st.title("Educational Tutor AI Assistant")

    st.sidebar.title("User Inputs")

    # Collect user inputs
    topic = st.sidebar.text_input("Topic for Quiz and Flashcards", "Introduction to Python Programming")
    text = st.sidebar.text_area("Text for Grammar Correction", "def my_function()\n print('Hello World')")
    project_topic = st.sidebar.text_input("Project Topic", "Building a Simple Calculator in Python")

    if st.sidebar.button("Generate Learning Materials"):
        with st.spinner('Generating content...'):
            # Run the Crew with user inputs
            crew_results = educational_tutor_crew.kickoff(
                inputs={
                    "topic": topic,
                    "text": text,
                    "project_topic": project_topic,
                }
            )

            # Display outputs
            display_outputs()

def display_outputs():
    st.header("Generated Quiz")
    with open(os.path.join(output_dir, "quiz.json"), "r") as f:
        quiz = json.load(f)

    st.subheader(f"Quiz Topic: {quiz['topic']}")
    for idx, question in enumerate(quiz['questions'], 1):
        st.write(f"**Question {idx}:** {question['question']}")
        options = '\n'.join([f"{i+1}. {opt}" for i, opt in enumerate(question['options'])])
        st.write(options)
        st.write(f"*Correct Answer: Option {question['correct_answer'] + 1}*")
        st.write("---")

    st.header("Generated Flashcards")
    with open(os.path.join(output_dir, "flashcards.json"), "r") as f:
        flashcards = json.load(f)

    st.subheader(f"Flashcards Topic: {flashcards['topic']}")
    for idx, card in enumerate(flashcards['cards'], 1):
        st.write(f"**Flashcard {idx}:**")
        st.write(f"**Front:** {card['front']}")
        st.write(f"**Back:** {card['back']}")
        st.write("---")

    st.header("Grammar Correction")
    with open(os.path.join(output_dir, "grammar_correction.json"), "r") as f:
        correction = json.load(f)

    st.subheader("Original Text")
    st.code(correction['original_text'])

    st.subheader("Corrected Text")
    st.code(correction['corrected_text'])

    st.subheader("Feedback")
    st.write(correction['feedback'])

    st.header("Project Guidance")
    with open(os.path.join(output_dir, "project_guidance.json"), "r") as f:
        guidance = json.load(f)

    st.subheader(f"Project Topic: {guidance['project_topic']}")
    st.write("**Resources:**")
    for resource in guidance['resources']:
        st.write(f"- {resource}")
    st.write("**Steps:**")
    for step in guidance['steps']:
        st.write(f"- {step}")
    st.write("**Tips:**")
    for tip in guidance['tips']:
        st.write(f"- {tip}")

if __name__ == "__main__":
    main()