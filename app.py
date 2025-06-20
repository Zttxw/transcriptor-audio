import streamlit as st
import requests
import os
import tempfile

st.title("🎧 Transcriptor de audio con IA (API de OpenAI)")

st.markdown("Sube tu archivo de audio y se transcribirá automáticamente usando el modelo `whisper-1` de OpenAI.")

openai_api_key = st.text_input("🔑 Ingresa tu clave de API de OpenAI", type="password")

uploaded_file = st.file_uploader("📤 Sube tu archivo de audio", type=["mp3", "wav", "m4a", "webm", "ogg", "opus"])

if uploaded_file and openai_api_key:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.info("⏳ Enviando archivo a OpenAI para transcripción...")

    with open(tmp_path, "rb") as audio_file:
        response = requests.post(
            "https://api.openai.com/v1/audio/transcriptions",
            headers={
                "Authorization": f"Bearer {openai_api_key}"
            },
            files={
                "file": (uploaded_file.name, audio_file, "audio/mpeg")
            },
            data={
                "model": "whisper-1"
            }
        )

    if response.status_code == 200:
        result = response.json()
        st.success("✅ Transcripción completada:")
        st.text_area("📄 Texto transcrito:", result["text"], height=250)
    else:
        st.error("❌ Error en la transcripción:")
        st.json(response.json())
