# Gemini Quizify
## Description
A streamlit app that can <ins>read documents and generate a quiz with 1-10 multiple-choice questions</ins> that allow users to test themselves.
## Demo

https://github.com/TommyCheng023/Gemini_Quizify/assets/115842289/969ee57c-46f4-4098-8494-0efb7fdb7a79


## Tutorial - Content
0. Basic Setup
1. PDF Processing
2. Embed Model
3. ChromaDB
4. Quiz Builder
5. Quiz Generator
6. Quiz Manager
7. Screen State Handling
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
### Streamlit Widgets
- `st.header()`: We should be familiar with that. This is the title of our app!
- `st.subheader()`: The header of a specific section in the app.
- `st.write()`: Display paragraphs.
- `st.text_input()`: A textbox for clients to type in something. You can add a placeholder for that.
  - `label`: You will have a line above the input block displaying a message if you assign a string to this parameter.
  - `placeholder`: Some transparent texts appears in the textbox, which will disappear if clients start typing things on the box.
- `st.slider()`: A slider for convenient inputs.
  - `label`: You will have a line above the input block displaying a message if you assign a string to this parameter.
  - `min_value`: The minimum value the slider can reach.
  - `max_value`: The maximum value the slider can reach.
  - `value`: The default value, or the value the slider is initially pointing to.

## 5. Quiz Generator
### System Template
When writing the `QuizGenerator` class, we can write a prompt-like paragraph to state the required formats for each question object.
```JSON
"question": "<question>",
"choices": [
  {{"key": "A", "value": "<choice>"}},
  {{"key": "B", "value": "<choice>"}},
  {{"key": "C", "value": "<choice>"}},
  {{"key": "D", "value": "<choice>"}}
],
"answer": "<answer key from choices list>",
"explanation": "<explanation as to why the answer is correct>"
```
### `QuizGenerator` Basic Structure
<img width="720" alt="Screen Shot 2024-03-16 at 6 49 32 PM" src="https://github.com/TommyCheng023/Gemini_Quizify/assets/115842289/693474f2-ee7b-4367-b21a-f2d1c9ab4a72">

### Quiz Demo (Raw Format in JSON)
https://github.com/TommyCheng023/Gemini_Quizify/assets/115842289/dbf5e05d-b94e-4f19-b6cb-3f4f61b626bc


## 6. Quiz Manager
- Use the user interface provided by `Streamlit` to make the generated quiz human-readable.
- Use `st.session_state[]` to store necessary information!

expected result:

<img width="802" alt="Screen Shot 2024-03-16 at 3 32 24 PM" src="https://github.com/TommyCheng023/Gemini_Quizify/assets/115842289/a7f53a35-a869-4366-bf54-5207fd4f72a1">

## 7. Screen State Handling
- new functionality: `Next Question`, `Previous Question` buttons
```python
# sample button that goes to the next question
st.form_submit_button("Next Question", on_click=lambda: obj.next_question_index(direction=1))
```
- related functions: `next_question_index()` from `QuizManager`, `get_question_at_index()` from `QuizManager`
  - recall the role of `direction`, the function should work if the algorithm is correct
  - remember to update your question when pressing the button
### Main Structure
1. Initialize your `PDF processor`, `embedding model` and create your `ChromaDB`.
2. Generate a `question_bank` and store it in your `st.session_state`.
3. Create a flag to let the app runs the quiz page once `question_bank` is ready.
4. `QuizManager` generates a user-friendly quiz page.
5. `Submit`, `Next Question`, `Previous Question` each performs the role correctly.
### ⚠️ Important Notes
1. The `if-else` structure stored in this repository cannot automatically refreshes the page to the quiz page since there's no specific command to rerun the app. You can solve it by clicking on the `Rerun` command that every Streamlit app has or add the following command to force rerun:
```python
st.experimental_rerun()
```
### Expected Result
<img width="792" alt="Screen Shot 2024-03-16 at 6 13 04 PM" src="https://github.com/TommyCheng023/Gemini_Quizify/assets/115842289/a1b144bf-54ed-4271-aa47-97a37315e512">

## Appendix
### Project Certificate
<ins>Coming Soon!</ins>
### Project Report
<ins>Coming Soon!</ins>
### Appreciation
- Appreciate Radical AI for providing such a precious experience on AI engineering and backend development.
- I also want to show my gratitude to Talha Sabri and Mikhail Ocampo for detailed instructions.
### About Contributors
- Mikhail Ocampo
  - GitHub Profile: [Mikhail.io](https://github.com/Vy-X-S)
- Xinyang(Tommy) Cheng
  - Personal Website: [About - Xinyang Cheng](https://tommycheng023.github.io/)
  - LinkedIn Profile: [Xinyang(Tommy) Cheng](www.linkedin.com/in/xinyang-cheng-325825260)
