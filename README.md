# Educational Tutor AI Assistant

An AI-powered educational assistant that helps learners improve skills like French, English, programming, or data analytics. The assistant includes features such as interactive quizzes, flashcards, real-time grammar correction, and project-based guidance in topics like Python, SQL, or Tableau.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
  - [Running the Jupyter Notebook](#running-the-jupyter-notebook)
  - [Running the Streamlit App](#running-the-streamlit-app)
- [API Key Configuration](#api-key-configuration)
- [Security Considerations](#security-considerations)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)

## Project Overview

The Educational Tutor AI Assistant utilizes advanced language models to generate educational content tailored to the user's needs. It harnesses the power of Google's Gemini AI models through the `litellm` and `crewai` libraries to provide interactive and personalized learning experiences.

## Features

- **Interactive Quizzes**: Generates multiple-choice quizzes on specified topics to test knowledge.
- **Flashcards Creation**: Creates flashcards for key concepts to aid memorization.
- **Real-time Grammar Correction**: Provides grammar corrections and feedback on input text.
- **Project Guidance**: Offers step-by-step guidance on projects in programming and data analytics.

## Project Structure

- `Educational_Tutor_AI_Assistant_Code_Walkthrough.ipynb`: Jupyter Notebook containing a detailed code walkthrough and explanations.
- `streamlit_app.py`: Streamlit application script that provides a web interface for interacting with the AI assistant.

## Requirements

- Python 3.7 or higher
- Python Packages:
  - `streamlit`
  - `crewai==0.95.0`
  - `litellm`
  - `pydantic`
  - `typing-extensions`
  - `python-dotenv`
  - `google-generativeai`

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/hafidaso/Educational_Tutor_AI_Assistant_Code_Walkthrough
   


2. **Set Up API Keys**

The application uses Google's Gemini AI models, which require an API key.

Create a .env File in the project root directory.

Add your API key to the .env file:

    
    GEMINI_API_KEY=your_gemini_api_key_here

## Usage

### Running the Jupyter Notebook

Launch Jupyter Notebook:

    
    jupyter notebook
    


Open 'Educational_Tutor_AI_Assistant_Code_Walkthrough.ipynb'.

This notebook contains a detailed walkthrough of the code, including explanations and code execution steps. Follow the instructions within the notebook to understand and execute each part.

### Running the Streamlit App

Run the Streamlit Application:

    streamlit run streamlit_app.py

Access the Application Interface:

Open your web browser and navigate to 'http://localhost:8501' (Streamlit will provide the exact URL upon running).

Interact with the AI Assistant:

**User Inputs**: Provide the topic for quizzes and flashcards, text for grammar correction, and project topic in the sidebar.

**Generate Content**: Click the "Generate Learning Materials" button.

**View Outputs**: The generated content will be displayed in the main area of the app.

## Security Considerations

- **API Key Protection**: Ensure that your API key remains confidential. Do not commit the `.env` file or any files containing the API key to version control systems like Git.
- **Monitor Usage**: Keep track of your API usage to avoid exceeding quotas or incurring unexpected charges.
- **Error Handling**: The application includes basic error handling to detect issues such as invalid API keys or exceeded quotas.

## Troubleshooting

- **Authentication Errors**: If you receive errors related to invalid API keys, double-check that your API key is correct and that the Generative Language API is enabled in your GCP project.
- **Module Not Found Errors**: Ensure all required packages are installed in your virtual environment.
- **Permission Issues**: Verify that your API key has the necessary permissions and that billing is enabled for your GCP project if required.
- **API Quota Exceeded**: Check your usage in the Google Cloud Console and consider requesting a quota increase or optimizing your API calls.

## Credits

- **Libraries Used**:
  - Streamlit - For building the web application interface.
  - CrewAI - For managing AI agents and tasks.
  - LiteLLM - For interfacing with language models.
  - Python-dotenv - For loading environment variables from a `.env` file.

- **Language Model**:
  - Google's Gemini Models via the Generative Language API.

## Author

**Hafida Belayd**

- [LinkedIn](https://www.linkedin.com/in/hafida-belayd/)
- [Colab Notebook](https://colab.research.google.com/drive/1vJgMUDS_HyBUKiKNnp4F8WVkqEJ3IiuO?usp=sharing)

## Acknowledgments

Thank you to the project that inspired this work:

**Abu Bakr Soliman, MSc**

- [LinkedIn](https://www.linkedin.com/in/bakrianoo)
- [Project Link](https://qabilah.com/posts/FuGZMgIyun0)