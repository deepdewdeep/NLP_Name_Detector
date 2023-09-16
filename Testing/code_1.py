# Core libraries
import streamlit as st 

# NLP libraries
import spacy_streamlit
import spacy
from spacy import displacy

def main():
    """A Streamlit NLP App with spaCy"""

    # Set page title and icon
    st.set_page_config(
        page_title="NLP App with spaCy", 
        page_icon="✅"
    )

    # Set app title and description
    st.title("Noun Detection App")
    st.markdown("This app performs tokenization and Named Entity Recognition (NER) using spaCy.")

    nlp = spacy.load("en_core_web_sm")

    # Get user input text
    st.subheader("Enter Text")
    raw_text = st.text_area("Input Text", "Enter your text here")

    if not raw_text.strip():
        st.warning("Please enter some text.")
        return

    # Perform actions based on user choice
    action = st.selectbox("Select an action", ["Tokenization", "NER Visualization"])

    if action == "Tokenization":
        st.subheader("Tokenization")
        docx = nlp(raw_text)
        spacy_streamlit.visualize_tokens(docx, attrs=['text','pos_','dep_','ent_type_'])

    elif action == "NER Visualization":
        st.subheader("Named Entity Recognition (NER)")
        docx = nlp(raw_text)
        
        # Display NER entities using spaCy's displaCy
        html = displacy.render(docx, style="ent")
        st.write(html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
