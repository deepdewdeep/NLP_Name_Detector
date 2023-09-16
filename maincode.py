import streamlit as st 
import matplotlib.pyplot as plt
import spacy_streamlit
import spacy
from spacy import displacy

def main():
    # Set page title and icon
    st.set_page_config(
        page_title="NLP App for Named Entity Recognition (NER)", 
        page_icon="🧠"
    )

    # Display the app title
    st.title("Named Entity Recognition App")

    # Load the English language model from spaCy
    nlp = spacy.load("en_core_web_sm")

    # Input Text Section
    st.subheader("Enter Text")
    raw_text = st.text_area("Input Text", "")

    # Check if input text is empty
    if not raw_text.strip():
        st.warning("Please enter some text.")
        return

    # Submit Button
    if st.button("Submit", key="submit_button"):
        # Tokenization Section
        st.subheader("Tokenization")
        docx = nlp(raw_text)
        
        # Extract part-of-speech tags from tokens
        pos_tags = [token.pos_ for token in docx]

        # Count the frequency of each part-of-speech tag
        pos_freq = {tag: pos_tags.count(tag) for tag in set(pos_tags)}

        # Create a bar chart for POS tags using Matplotlib
        plt.figure(figsize=(10, 6))
        plt.bar(pos_freq.keys(), pos_freq.values())
        plt.xlabel("Part of Speech")
        plt.ylabel("Frequency")
        plt.title("Part of Speech Frequency")
        plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility

        # Display the Matplotlib chart in Streamlit
        st.pyplot(plt)

        # Named Entity Recognition (NER) Visualization Section
        st.subheader("Named Entity Recognition (NER)")
        
        # Display NER entities using spaCy's displaCy with custom style
        html = displacy.render(docx, style="ent")
        st.write(html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
