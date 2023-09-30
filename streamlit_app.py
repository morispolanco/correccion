import streamlit as st
from docx import Document
from googletrans import Translator
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

def translate_text(text, target_lang):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

def compare_documents(original_doc, translated_doc):
    changes = []
    for i in range(len(original_doc.paragraphs)):
        original_text = original_doc.paragraphs[i].text
        translated_text = translated_doc.paragraphs[i].text
        if original_text != translated_text:
            changes.append((original_text, translated_text))
    return changes

def save_changes(changes):
    doc = Document()
    for original_text, translated_text in changes:
        p = doc.add_paragraph()
        p.add_run("Original: ").bold = True
        p.add_run(original_text)
        p.add_run("\n")
        p.add_run("Traducción: ").bold = True
        p.add_run(translated_text)
        p.add_run("\n")
        p.add_run("-" * 50)
        p.add_run("\n")
    doc.save("control_de_cambios.docx")

def main():
    st.title("Traductor y comparador de documentos")
    st.write("Cargue un documento en español para traducirlo y compararlo con la traducción final:")
    
    file = st.file_uploader("Cargar documento .docx", type=["docx"])
    
    if file is not None:
        original_doc = Document(file)
        
        st.write("Documento original:")
        for paragraph in original_doc.paragraphs:
            st.write(paragraph.text)
        
        translated_text = translate_text(original_doc.text, "en")
        translated_doc = Document()
        translated_doc.add_paragraph(translated_text)
        
        st.write("Documento traducido al inglés:")
        for paragraph in translated_doc.paragraphs:
            st.write(paragraph.text)
        
        retranslated_text = translate_text(translated_text, "es")
        retranslated_doc = Document()
        retranslated_doc.add_paragraph(retranslated_text)
        
        st.write("Documento traducido nuevamente al español:")
        for paragraph in retranslated_doc.paragraphs:
            st.write(paragraph.text)
        
        changes = compare_documents(original_doc, retranslated_doc)
        
        st.write("Cambios realizados:")
        for original_text, translated_text in changes:
            st.write("Original:", original_text)
            st.write("Traducción:", translated_text)
            st.write("-" * 50)
        
        save_changes(changes)
        st.write("Control de cambios guardado como 'control_de_cambios.docx'")

if __name__ == "__main__":
    main()
