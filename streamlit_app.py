import streamlit as st
from googletrans import Translator, LANGUAGES
from docx import Document
from diff_match_patch import diff_match_patch

st.title("Traducción y comparación de documentos")

# Carga del archivo
uploaded_file = st.file_uploader("Carga un documento Word", type="docx")
if uploaded_file is not None:
    doc = Document(uploaded_file)

    # Traducción al inglés
    translator = Translator()
    translated_texts = []
    for paragraph in doc.paragraphs:
        translated_texts.append(translator.translate(paragraph.text, src='es', dest='en').text)

    # Nuevo documento en inglés
    doc_en = Document()
    for text in translated_texts:
        doc_en.add_paragraph(text)

    # Traducción del inglés al español
    translated_texts_es = []
    for paragraph in doc_en.paragraphs:
        translated_texts_es.append(translator.translate(paragraph.text, src='en', dest='es').text)

    # Nuevo documento en español
    doc_es = Document()
    for text in translated_texts_es:
        doc_es.add_paragraph(text)

    # Comparación
    diff = diff_match_patch()
    diff_result = diff.diff_main(doc.text, doc_es.text)
    diff.diff_cleanupSemantic(diff_result)
    diff_text = diff.diff_prettyHtml(diff_result)

    # Visualización de la comparación
    st.write(diff_text, unsafe_allow_html=True)

    # Descarga del documento comparado
    def filedownload(doc, name):
        doc.save(name)
        st.download_button(
            label="Descargar documento comparado",
            data=doc,
            file_name=name,
            mime="application/octet-stream"
        )

    filedownload(doc_es, "documento_comparado.docx")
