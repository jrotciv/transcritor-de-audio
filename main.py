import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio, language="pt-BR")
            return text
        except sr.UnknownValueError:
            return "[Inaudível]"
        except sr.RequestError as e:
            return f"[Erro na solicitação de reconhecimento de fala: {e}]"

audio_files = ["./audioteste.wav"]

transcriptions = [transcribe_audio(file) for file in audio_files]

with open("transcriptions.txt", "w") as file:
    for idx, transcription in enumerate(transcriptions):
        file.write(f"Transcrição do áudio {idx+1}:\n")
        file.write(transcription + "\n\n")

print("Transcrições salvas em 'transcriptions.txt'")
