# pdf_processing.py

# Necessary imports
import streamlit as st
import PyPDF2
import os
import tempfile
import uuid

class DocumentProcessor:
    """
    This class encapsulates the functionality for processing uploaded PDF documents using Streamlit
    and Langchain's PyPDFLoader. It provides a method to render a file uploader widget, process the
    uploaded PDF files, extract their pages, and display the total number of pages extracted.
    """
    def __init__(self):
        self.pages = []  # List to keep track of pages from all documents
    
    def ingest_documents(self):
        """
        Renders a file uploader in a Streamlit app, processes uploaded PDF files,
        extracts their pages, and updates the self.pages list with the total number of pages.
        
        Given:
        - Handling of temporary files with unique names to avoid conflicts.
        
        Your Steps:
        1. Utilize the Streamlit file uploader widget to allow users to upload PDF files.
           Hint: Look into st.file_uploader() with the 'type' parameter set to 'pdf'.
        2. For each uploaded PDF file:
           a. Generate a unique identifier and append it to the original file name before saving it temporarily.
              This avoids name conflicts and maintains traceability of the file.
           b. Use Langchain's PyPDFLoader on the path of the temporary file to extract pages.
           c. Clean up by deleting the temporary file after processing.
        3. Keep track of the total number of pages extracted from all uploaded documents.
        
        Example for generating a unique file name with the original name preserved:
        ```
        unique_id = uuid.uuid4().hex
        temp_file_name = f"{original_name}_{unique_id}{file_extension}"
        ```
        """
        
        # Render a file uploader widget: accept PDF only and accept multiple files 
        uploaded_files = st.file_uploader("Upload a PDF file", type="pdf", accept_multiple_files=True)
        
        if uploaded_files is not None:
            for uploaded_file in uploaded_files:
                # Generate a unique identifier to append to the file's original name
                unique_id = uuid.uuid4().hex
                original_name, file_extension = os.path.splitext(uploaded_file.name)
                temp_file_name = f"{original_name}_{unique_id}{file_extension}"
                temp_file_path = os.path.join(tempfile.gettempdir(), temp_file_name)

                # Write the uploaded PDF to a temporary file
                with open(temp_file_path, 'wb') as f:
                    f.write(uploaded_file.getvalue())

                # Process the temporary file
                """
                    https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf#using-pypdf
                    Use PyPDFLoader here to load the PDF and extract pages.
                    You will need to figure out how to use PyPDFLoader to process the temporary file.
                """
                # Process the file if there exists
                if uploaded_file is not None:
                    pdf_reader = PyPDF2.PdfReader(uploaded_file)
                    num_pages = len(pdf_reader.pages)
                    st.write(f"The PDF contains {num_pages} pages.")

                # Step 3: Then, Add the extracted pages to the 'pages' list.
                #####################################
                if uploaded_file is not None:
                    for page_number in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_number]
                        self.pages.append(page.extract_text())

                # Clean up by deleting the temporary file.
                os.unlink(temp_file_path)
            
            # Display the total number of pages processed.
            st.write(f"Total pages processed: {len(self.pages)}")
        
if __name__ == "__main__":
    processor = DocumentProcessor()
    processor.ingest_documents()
