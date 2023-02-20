import sys
import time
import os
# import torch
# import subprocess

st_total = time.monotonic()

def get_whisper():
    sys.path.insert(0, '../whisper')
    import whisper
    model = whisper.load_model("base")
    return model


# def get_model():
#     # Define the path to the cache file
#     cache_path = "buddy/whisper_cache/my_model_cache.pt"

#     # Check if the cache file exists
#     if os.path.exists(cache_path):
#         # If the cache file exists, load the model's state dictionary from the file
#         print("found cached whisper...")
#         # model = whisper.load_model("base")
#         model.load_state_dict(torch.load(cache_path))

#     else:
#         # If the cache file does not exist, import the model and save its state dictionary to the cache file
#         sys.path.insert(0, '../whisper')
#         import whisper
#         model = whisper.load_model("base")

#         torch.save(model.state_dict(), cache_path)

#     return model

print("----------------getting whisper---------------")
model = get_whisper()
print("----------------whisper transcribing---------------")
st_transcribe = time.monotonic()
# result = model.transcribe("output.wav")
result = model.transcribe("output.wav")
# result = model.transcribe("buddy/LJ037-0171.wav")
et_transcribe = time.monotonic() - st_transcribe
print(f"\n Transcribing took took: {et_transcribe*1000:.2f} ms\n")
print("-----------------------------------")



# print(result["text"])

# python3 buddy/gpt2.py \
#     --init_from=gpt2-xl \
#     --start="What is the answer to life, the universe, and everything?" \
#     --num_samples=5 --max_new_tokens=100

prompt = '"' + result['text'] + '"' 
print("transcription::::",prompt)
print("")

str = f"python3 buddy/gpt2.py --init_from=gpt2 --start=" + prompt +""

print("-----------------------------------")
print("")
print("str:")
# print(str)
st_gpt2 = time.monotonic()
os.system(str)
et_gpt2 = time.monotonic() - st_gpt2
print(f"\n GPT-2 time took: {et_gpt2*1000:.2f} ms\n")
print("")
print("-----------------------------------")

et_total = time.monotonic() - st_total

print(f"\n Total inference time took: {et_total*1000:.2f} ms\n")