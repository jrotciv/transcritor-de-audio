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

audio_file = "./audioteste.wav"

transcription = transcribe_audio(audio_file)

with open("transcriptions.txt", "w") as file:
    file.write("Transcrição do áudio:\n")
    file.write(transcription + "\n")

print("Transcrição salva em 'transcriptions.txt'")
