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
        page_title="NLP App for Named Entity Recognition (NER)", 
        page_icon="🧠"
    )

    # Set app title and description with custom style
    st.title("Named Entity Recognition App")
    st.markdown(
        """
        <style>
        /* Add some custom CSS styles */
        .stApp {
            background-color: #f0f0f0; /* Change the background color */
            padding: 2rem;
            border-radius: 10px;
        }
        .stTitle {
            font-size: 36px; /* Increase title font size */
            color: #333; /* Change title color */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    nlp = spacy.load("en_core_web_sm")

    # Get user input text
    st.subheader("Enter Text")
    raw_text = st.text_area("Input Text", "")

    if not raw_text.strip():
        st.warning("")
        return

    # Add a submit button with custom style
    if st.button("Submit", key="submit_button"):
        # Perform actions based on user choice
        action = "NER Visualization"

        if action == "Tokenization":
            st.subheader("Tokenization")
            docx = nlp(raw_text)
            spacy_streamlit.visualize_tokens(docx, attrs=['text','pos_','dep_','ent_type_'])

        elif action == "NER Visualization":
            st.subheader("Named Entity Recognition (NER)")
            docx = nlp(raw_text)
            
            # Display NER entities using spaCy's displaCy with custom style
            html = displacy.render(docx, style="ent")
            st.write(html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
