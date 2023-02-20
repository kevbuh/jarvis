from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")

if __name__ == "__main__":
    print("yuhhhhh hf gpt j")