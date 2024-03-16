# Gemini Quizify
## Demo
<ins>Coming Soon!</ins>

## Tutorial - Content
0. Basic Setup
1. PDF Processing
2. Embed Model
3. ChromaDB
4. Quiz Builder
5. Quiz Generator
6. Quiz Manager
## 0. Basic Setup
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

## 1. PDF Processing
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

## 2. Embed Model
<img width="526" alt="Screen Shot 2024-03-15 at 9 49 40 PM" src="https://github.com/TommyCheng023/Gemini_Quizify/assets/115842289/5e9a95e6-d562-4356-8b68-59ee63fb0c74">

### Reference
[Langchain Text_Embedding](https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai)

## 3. ChromaDB
- Work on data transformation and collection with `ChromaDB`, an open-source embedding database!
<img width="725" alt="Screen Shot 2024-03-16 at 11 07 46 AM" src="https://github.com/TommyCheng023/Gemini_Quizify/assets/115842289/473b19d2-f539-4701-9230-7261b79e46bf">

- Ensure document processing, split text chunks using `CharacterTextSplitter`, and create a Chroma collection in memory. 

<img width="754" alt="Screen Shot 2024-03-15 at 9 51 27 PM" src="https://github.com/TommyCheng023/Gemini_Quizify/assets/115842289/b0c73b14-ce16-4a4f-b80e-77edf05b6983">

### Task Breakdown
1. Import `processor` and `embedding model` classes from the previous files.
2. Build a new function creating the `ChromaDB`.
3. Check if the document exists.
4. Split the document into text chunks for embedding and indexing using [`CharacterTextSplitter`](https://python.langchain.com/docs/modules/data_connection/document_transformers/) imported from `Langchain`.
5. Use [`Chroma.from_documents()`](https://docs.trychroma.com/getting-started) to create a Chroma Collection.
### ⚠️ Important Notes
1. Remember to run the file in the correct path (the folder containing `DBCollection.py`) since our way of importing classes looks like this:
```python
sys.path.append(os.path.abspath('../../'))    # trace back to the parent folder for two times
from tasks.task_3.task_3 import DocumentProcessor
from tasks.task_4.task_4 import EmbeddingClient
```
thus to run the file, you need to type in this command:
```sh
streamlit run DBCollection.py
```
2. `Chroma.from_documents()` requires **a string object contains the attribute `page-content`, as well as an embedding function to compute** as parameters. Hence we need to use the `Document()` class imported from `langchain`. Recall we have `texts` defined to collect the splitted text chunks, which its length is needed to be part of the response to the client. We can create a new empty list and apply a `for` loop to go over every object stored in `texts` and create a `Document` object for each of them, then store them into the new declared list using `append()`. **Reminder `Document()` from `langchain` accepts only ONE positional argument, so don't put anything else inside.** 

## 4. Quiz Builder
Task: Build a Quiz Builder with `Streamlit` and `LangChain` with classes built before.

## 5. Quiz Generator

## 6. Quiz Manager