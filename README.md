# Gemini Quizify
## PDF Processing
<img width="804" alt="Screen Shot 2024-03-15 at 2 20 03 PM" src="https://github.com/TommyCheng023/Gemini_Quizify/assets/115842289/d2a24864-eb36-423c-a8cb-914c0e3c6e0e">

## Common Issue With Solution
1. Module installed and imported but module not found when running Streamlit.

  **solution: check your `site-package` through a terminal; shut down your code editor and reopen it; delete your virtual environment and remake one**

2. `Langchain` is not working.
 
  **solution: replace it with `PyPDF2`**
