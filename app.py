import whisper
import gradio as gr

# Cargar modelo de Whisper
model = whisper.load_model("base")

# Función de transcripción
def transcribe(audio):
    if audio is None:
        return "Por favor, sube un archivo de audio."
    result = model.transcribe(audio)
    return result["text"]

# Interfaz con Gradio
interface = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(sources=["upload"], type="filepath", label="Sube tu audio (MP3, WAV, etc.)"),
    outputs="text",
    title="Transcriptor de Audio",
    description="Sube tu archivo de audio y obtén la transcripción automáticamente usando Whisper.",
)

interface.launch()
