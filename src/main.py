from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Carrega modelo básico (ex: GPT-2 pequeno)
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Função de geração com semente de questionamento
def generate_with_questions(prompt, max_length=50):
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
    output = generator(prompt, max_length=max_length, num_return_sequences=1)
    
    # Simulação de "autoquestionamento" (placeholder)
    if "?" in prompt:
        return output[0]["generated_text"] + " [QUESTION]: Por que essa resposta faz sentido?"
    return output[0]["generated_text"]

# Teste
if __name__ == "__main__":
    prompt = "A ética na IA é importante porque"
    response = generate_with_questions(prompt)
    print(response)
