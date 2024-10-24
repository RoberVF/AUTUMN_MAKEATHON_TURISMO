from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Cargamos el modelo
model= GPT2LMHeadModel.from_pretrained("./fine_tuning/fine_tuned_model")
tokenizer= GPT2Tokenizer.from_pretrained("./fine_tuning/fine_tuned_model")

# DistilGPT-2 no tiene un pad_token por defecto, a si que usaremos el de eos_token
tokenizer.pad_token= tokenizer.eos_token

# Entrada de texto
input_text= input("Pregunta: ")

# Parametros
max_size = 160
size_to_start_to_finish= 70

# Generamos el texto
inputs= tokenizer(input_text, return_tensors= "pt", padding= True)

output= model.generate(
    inputs['input_ids'], 
    attention_mask=inputs['attention_mask'], 
    max_length= max_size,
    min_length= 25,
    num_beams= 10,
    temperature= 0.7,
    no_repeat_ngram_size= 2,
    top_p= 0.9,
    eos_token_id= tokenizer.eos_token_id
    )

generated_text= tokenizer.decode(output[0], skip_special_tokens= True)

# Dividimos el texto en palabras para comprobar las finalizaciones de las frases
words = generated_text.split()

# Cortamos la frase a partir de la palabra numero size_to_start_to_finish para generar la frase coherente
final_text= []
for i, word in enumerate(words):
    final_text.append(word)
    if i >= size_to_start_to_finish and word.endswith((".", "?", "!", "...")):
        break

final_text = " ".join(final_text)

print(f"\nRespuesta: {final_text}")