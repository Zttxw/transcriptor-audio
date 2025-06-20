import streamlit as st
import whisper
import tempfile

# CSS personalizado
st.markdown("""
    <style>
    .main-title {
        font-size:38px;
        text-align:center;
        color:#4F8BF9;
        margin-bottom: 10px;
    }
    .sub-text {
        text-align:center;
        color: #888;
        font-size: 16px;
    }
    </style>
    <div class="main-title">🎧 Transcriptor de Audio con IA</div>
    <div class="sub-text">Convierte archivos de audio a texto con un solo clic</div>
""", unsafe_allow_html=True)

st.sidebar.title("ℹ️ Ayuda")
st.sidebar.markdown("**Formatos compatibles**: MP3, WAV, OGG, M4A, OPUS")

uploaded_file = st.file_uploader("📤 Sube tu archivo", type=["mp3", "wav", "ogg", "m4a", "opus", "webm"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        audio_path = tmp.name

    st.info("⏳ Transcribiendo...")
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)

    st.success("✅ Transcripción completa:")
    st.text_area("📄 Texto:", result["text"], height=250)
