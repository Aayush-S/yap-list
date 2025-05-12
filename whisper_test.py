import whisper

model = whisper.load_model("turbo")
result = model.transcribe("short.mp3")

print(result["text"])