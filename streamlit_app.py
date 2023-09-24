import streamlit as st
import requests
import json

def translate_to_english(text):
    url = "https://ai-translate.pro/api/{secret_key}/es-en"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "text": text
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    result = response.json()

    return result["result"]

def translate_to_spanish(text):
    url = "https://ai-translate.pro/api/9428f69325adc980cc9b9dc6a0f84a30a3eb86e74787792c581cc44e4c1adfae/en-es"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "text": text
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    result = response.json()

    return result["result"]

def compare_texts(original_text, translated_text):
    if original_text == translated_text:
        return "Los textos son iguales."
    else:
        return "Los textos son diferentes."

def save_comparison(original_text, translated_text):
    with open("comparison.docx", "w") as file:
        file.write(f"Texto original: {original_text}\n")
        file.write(f"Texto traducido: {translated_text}\n")

def main():
    st.title("Traductor y Comparador de Texto")
    st.write("Ingrese el texto en Español:")
    original_text = st.text_area("Texto original")
    
    if st.button("Traducir al Inglés"):
        translated_text = translate_to_english(original_text)
        st.write("Texto traducido al Inglés:")
        st.write(translated_text)
        
        if st.button("Traducir al Español"):
            translated_back_text = translate_to_spanish(translated_text)
            st.write("Texto traducido al Español:")
            st.write(translated_back_text)
            
            comparison_result = compare_texts(original_text, translated_back_text)
            st.write("Comparación de textos:")
            st.write(comparison_result)
            
            if st.button("Guardar comparación"):
                save_comparison(original_text, translated_back_text)
                st.write("Comparación guardada con éxito.")

if __name__ == "__main__":
    main()
