import sys

sys.path.insert(0, '../whisper')

import whisper

model = whisper.load_model("base")
result = model.transcribe("buddy/LJ037-0171.wav")
print(result["text"])