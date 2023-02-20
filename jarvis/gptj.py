# https://huggingface.co/docs/transformers/model_doc/gptj
from transformers import AutoTokenizer, AutoModelForCausalLM, GPTJForCausalLM
import torch


device_type = 'mps' if torch.backends.mps.is_available() else 'cpu' # for later use in torch.autocast, i changed this from cude to mps

print(f"working, using {device_type}")
print(torch.__version__)


model = GPTJForCausalLM.from_pretrained(
    "EleutherAI/gpt-j-6B",
    revision="float16", 
    torch_dtype=torch.float16, 
    low_cpu_mem_usage=True
)

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")


prompt = (
    "What is homework"
)

input_ids = tokenizer(prompt, return_tensors="pt").input_ids

print("generating")

gen_tokens = model.generate(
    input_ids,
    do_sample=True,
    temperature=0.9,
    max_length=50,
)

gen_text = tokenizer.batch_decode(gen_tokens)[0]

print(f"generated this::::::::: {gen_text}")