import streamlit as st
from PIL import Image
import io

# Configuração da página
st.set_page_config(page_title="Conversor de Imagem para PDF", page_icon="📄")

# ASCII Art
ascii_art = """
 _  _      _____   _____ ____    ____  ____  _____
/ \/ \__/|/  __/  /__ __Y  _ \  /  __\/  _ \/    /
| || |\/||| |  _    / \ | / \|  |  \/|| | \||  __\
| || |  ||| |_//    | | | \_/|  |  __/| |_/|| |   
\_/\_/  \|\____\    \_/ \____/  \_/   \____/\_/   
                                                     
"""

st.text(ascii_art)

st.title("🖼️ Imagem para PDF")
st.write("Suba sua imagem e baixe o PDF convertido instantaneamente.")

# Widget de Upload
uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Exibe uma prévia da imagem
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagem carregada", use_container_width=True)

    # Botão para converter
    if st.button("Converter para PDF"):
        # Lógica de conversão em memória
        pdf_buffer = io.BytesIO()
        
        # Garante que está em RGB (essencial para PDF)
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
        
        image.save(pdf_buffer, format="PDF")
        pdf_buffer.seek(0)

        # Botão de Download (aparece após a conversão)
        st.download_button(
            label="📥 Baixar PDF",
            data=pdf_buffer,
            file_name="convertido.pdf",
            mime="application/pdf"
        )
        st.success("Conversão concluída!")
