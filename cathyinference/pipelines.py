from transformers import pipeline


# TODO: mount a volume so this can be used in a docker container
prompt_guard = pipeline("text-classification", model="meta-llama/Prompt-Guard-86M")

# TODO: give this chat more structure, memory, break input into user and system prompts
chatty_cathy = pipeline("text-generation", model="meta-llama/Llama-3.1-8B-Instruct")