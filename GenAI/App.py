# Importing libraries
import streamlit as st
import StreamlitFileHandling
import matplotlib.pyplot as plt
from GenAIProject_1 import FileHandling
from GenAIProject_1 import MarkdownConversion
from GenAIProject_2 import Text_Ingestion
from GenAIProject_2 import Text_Tokenization
from GenAIProject_2 import Text_Entity_Recongnition
from GenAIProject_2 import Text_Summary_Generator
from GenAIProject_2 import Output_Generation
import Config

# Inject CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/free-vector/realistic-neon-lights-background_23-2148907367.jpg?t=st=1745501958~exp=1745505558~hmac=3e81f2c79c39fa1dd38d708b741d7d323ba1ec31621f41dca3e3d3c4362aa23b&w=1380");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("GenAI Text Processor")
import streamlit as st

# Set allowed types
uploaded_file = st.file_uploader("Upload your file", type=["pdf", "txt", "wav", "docx", "mp3"], key="unique_file_uploader")

if uploaded_file is not None:
    st.success(f"Uploaded file: {uploaded_file.name}")
    filepath = StreamlitFileHandling.save_uploaded_file(uploaded_file)

    #Validating the file existence or if the file is supported or not
    validate_msg = FileHandling.validate_file(filepath)

    st.badge(validate_msg)

    # Automatic file detection
    FileHandling.detect_file_type(filepath)

    # File Extraction and conversion into Markdown
    MarkdownConversion.convert_to_markdown(filepath)

    # Converting the markdown text into plain text
    plain_text = Text_Ingestion.extract_text(Config.inputFilePath)

      # Cleaning the Plain text
    clean_text = Text_Ingestion.clean_text(plain_text)

    # Performing Tokenization
    tokens = Text_Tokenization.get_word_tokens(clean_text)

    #Performing NER
    tokens,tagged_wordnet, ner_tree = Text_Entity_Recongnition.perform_ner(clean_text)

    # Summarizing text
    text_summary = Text_Summary_Generator.content(clean_text)

    st.header("Text Summary: ")
    st.write(text_summary)
    st.write("\n")

    option = st.selectbox("Select an Operation",
        ("Display Tokens", "Display Part of Speech Tags", "Display Named Entities"),
        index=None
    )
    if option=="Display Tokens":
        st.header("Tokens: ")
        st.write(tokens)

    elif option=="Display Part of Speech Tags":
        st.header("Part of Speech Tags: ")
        st.write(tagged_wordnet)

    elif option=="Display Named Entities":
        st.header("Named Entity Recongnition: ")
        st.write(ner_tree)

    #Saving the output
    output = Output_Generation.save_to_file(text_summary,ner_tree)

    st.download_button(
    label="Download File",
    data= output,
    file_name="output_summary.txt",
    mime="text/txt",
    icon=":material/download:",
)
