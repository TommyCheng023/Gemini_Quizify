# Gemini Quizify
## Tutorial - Content
0. Basic Setup
1. PDF Processing
2. Embed Model
3. ChromaDB
## Basic Setup
- create a new project on Google Cloud Console, you can name it as <i>Gemini Quizify</i>
  - go to `vertexAI` and click `enable all recommended APIs`
  - search for `Service Accounts` and create a new service account, set role as `basic - owner` and download the authentication key as a JSON file
  - put the file into your project and update `.gitignore` to ignore that file, then type the command
```sh
export GOOGLE_APPLICATION_CREDENTIALS = "/path/to/your/authentication-file.json"
```
- build a virtual environment (optional but highly recommended)
  - remember to update `.gitignore` to ignore the environment folder
```sh
python3 -m venv env
```
```sh
source env/bin/activate
```
- install necessary packages
```sh
pip install -r requirements.txt
```

## PDF Processing
A file uploader is needed for the app.

<img width="804" alt="Screen Shot 2024-03-15 at 2 20 03 PM" src="https://github.com/TommyCheng023/Gemini_Quizify/assets/115842289/d2a24864-eb36-423c-a8cb-914c0e3c6e0e">

### Common Issue With Solution
1. Module installed and imported but module not found when running Streamlit.

  **solution: check your `site-package` through a terminal; shut down your code editor and reopen it; delete your virtual environment and remake one**

2. `Langchain` is not working.
 
  **solution: replace it with `PyPDF2`, remember to install it first**
```sh
pip install PyPDF2
```

## Embed Model
<img width="526" alt="Screen Shot 2024-03-15 at 9 49 40 PM" src="https://github.com/TommyCheng023/Gemini_Quizify/assets/115842289/5e9a95e6-d562-4356-8b68-59ee63fb0c74">
### Reference
[Langchain Text_Embedding](https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai)

## ChromaDB
- Work on data transformation and collection with `ChromaDB`!
- Ensure document processing, split text chunks using `CharacterTextSplitter`, and create a Chroma collection in memory. 

<img width="754" alt="Screen Shot 2024-03-15 at 9 51 27 PM" src="https://github.com/TommyCheng023/Gemini_Quizify/assets/115842289/b0c73b14-ce16-4a4f-b80e-77edf05b6983">

### ⚠️ Important Notes
