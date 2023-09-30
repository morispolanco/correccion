import streamlit as st
import docx2txt
import docx
import requests

# Función para traducir el texto utilizando la API de AI Translate
def translate_text(text, source_lang, target_lang):
    url = "https://ai-translate.pro/api/9428f69325adc980cc9b9dc6a0f84a30a3eb86e74787792c581cc44e4c1adfae/{}/{}".format(source_lang, target_lang)
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "text": text
    }
    response = requests.post(url, headers=headers, json=data)
    translation = response.json()
    return translation["text"]

# Configuración de la aplicación de Streamlit
st.title("Traductor y comparador de documentos")

# Cargar el documento DOCX en español
uploaded_file = st.file_uploader("Cargar documento DOCX en español", type="docx")

if uploaded_file is not None:
    # Convertir el documento a texto en español
    text_es = docx2txt.process(uploaded_file)
    
    # Traducir el texto al inglés
    text_en = translate_text(text_es, "es", "en")
    
    # Traducir el texto en inglés de nuevo al español
    text_es_translated = translate_text(text_en, "en", "es")
    
    # Comparar el primer documento en español y el último documento traducido al español
    comparison = "Los documentos son iguales." if text_es == text_es_translated else "Los documentos son diferentes."
    
    # Crear un nuevo documento DOCX con las comparaciones
    new_doc = docx.Document()
    new_doc.add_paragraph("Documento original en español:")
    new_doc.add_paragraph(text_es)
    new_doc.add_paragraph("Documento traducido al español:")
    new_doc.add_paragraph(text_es_translated)
    new_doc.add_paragraph("Comparación:")
    new_doc.add_paragraph(comparison)
    
    # Descargar el nuevo documento DOCX
    st.download_button("Descargar documento con comparaciones", data=docx.save(new_doc), file_name="documento_comparado.docx")
