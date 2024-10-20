from datasets import load_dataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments

dataset = load_dataset('json', data_files="fine_tuning.json")

model= GPT2LMHeadModel.from_pretrained("datificate/gpt2-small-spanish")
tokenizer= GPT2Tokenizer.from_pretrained("datificate/gpt2-small-spanish")

max_size= 160

def preprocess(qa):
    # Cargamos todas las questions y answers de fine_tuning.json
    inputs= [question for question in qa['question']]
    outputs= [answer for answer in qa['answer']]

    model_inputs= tokenizer(inputs, max_length=max_size, truncation=True, padding="max_length")

    with tokenizer.as_target_tokenizer():
        labels= tokenizer(outputs, max_length=max_size, truncation=True, padding="max_length")

    model_inputs['labels']= labels['input_ids']

    return model_inputs

# Se tokeniza el conjunto del dataset
tokenized_dataset= dataset.map(preprocess, batched=True)

fine_tune_args= TrainingArguments(
    output_dir= './fine_tuning_results',
    save_strategy= 'epoch',
    evaluation_strategy= 'epoch', # Evalua al final de cada epoca
    learning_rate= 2e-5, # Valor comun para la tasa de aprendizaje
    per_device_train_batch_size= 4, # Size del lote a evaluar
    num_train_epochs= 3, # Veces q evaluamos el conjunto de datos
    weight_decay= 0.01 # Prevenir el sobreajuste. Tenemos un modelo mas simple pero no necesitamos mas :D

    # Ajustar el size del lote en base a la memoria disponible de la Rasp. Probamos con 4 y vamos subiendo
)

fine_tune= Trainer(
    model= model,
    args= fine_tune_args,
    train_dataset= tokenized_dataset['train'],
    eval_dataset= tokenized_dataset['train']
)

fine_tune.train()

# Guardamos el modelo entrenado
model.save_pretrained('./fine_tuned_model')
tokenizer.save_pretrained('./fine_tuned_model')