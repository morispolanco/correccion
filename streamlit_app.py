import streamlit as st

def main():
    st.title("Formulario de carga de documentos")

    # Mostrar el formulario para ingresar el nombre y la dirección de correo electrónico
    name = st.text_input("Nombre")
    email = st.text_input("Correo electrónico")

    # Mostrar el formulario para cargar el documento
    uploaded_file = st.file_uploader("Cargar documento")

    if uploaded_file is not None:
        # Guardar el archivo cargado en el servidor
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Mostrar un mensaje de éxito
        st.success("El documento se ha cargado correctamente.")

        # Mostrar un enlace para descargar el documento
        st.download_button("Descargar documento", uploaded_file.name, "Documento cargado")

if __name__ == "__main__":
    main()
