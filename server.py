from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


saved_model_dir = "./trained_model"
model_url = "Helsinki-NLP/opus-mt-en-ru"

tokenizer = AutoTokenizer.from_pretrained(model_url)
model = AutoModelForSeq2SeqLM.from_pretrained(model_url)




def predict(input_text):
    # Предобработка входных данных
    input_ids = tokenizer.encode(input_text, return_tensors="pt")   
    # Передача данных в модель
    output_ids = model.generate(input_ids, max_length=128, num_beams=4, early_stopping=True)
    # Декодирование выходных данных
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return output_text



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def ans():
    result = predict(request.json['text'])
    return jsonify(result)

if __name__ == '__main__':
    app.run()
