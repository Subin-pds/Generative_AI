#Importing reuired libraries
from GenAIProject_1 import FileHandling
from GenAIProject_1 import MarkdownConversion
from GenAIProject_2 import Text_Ingestion
from GenAIProject_2 import Text_Tokenization
from GenAIProject_2 import Text_Entity_Recongnition
from GenAIProject_2 import Text_Summary_Generator
from tkinter import filedialog
import Config

  # Open the file dialog
filepath = filedialog.askopenfilename(title = "Select a file")
filepath = r"{}".format(filepath)
print(filepath)

#Validating the file existence or if the file is supported or not
FileHandling.validate_file(filepath)

# Automatic file detection
FileHandling.detect_file_type(filepath)

# File Extraction and conversion into Markdown
MarkdownConversion.convert_to_markdown(filepath)

# Converting the markdown text into plain text
plain_text = Text_Ingestion.extract_text(Config.inputFilePath)

# Cleaning the Plain text
clean_text = Text_Ingestion.clean_text(plain_text)

# Performing Tokenization
#tokens = Text_Tokenization.get_word_tokens(clean_text)

#Performing NER
tokens_filtered, pos_groups, ner_tree = Text_Entity_Recongnition.perform_ner(clean_text)

#Summarizing text
text_summary = Text_Summary_Generator.content(clean_text)