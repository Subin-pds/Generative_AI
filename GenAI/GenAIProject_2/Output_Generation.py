import os

def save_to_file(summary, ner, filename="output_summary.txt"):
    """Save the summary and NER results to a text file."""

    filename = os.path.join("Data","Output",filename)
    # Ensure the directory exists
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Write to the file
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Summary:\n")
        file.write(summary + "\n\n")
        file.write("Named Entities:\n")
        for entity, label in ner:
            file.write(f"{entity} ({label})\n")
    with open(filename, "r") as file:
        text = file.read()
    return text
