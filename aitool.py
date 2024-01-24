# app.py
from flask import Flask, render_template, request, jsonify
from langchain_openai import ChatOpenAI
from flask_cors import CORS

app = Flask(__name__)
llm = ChatOpenAI(openai_api_key="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")

@app.route('/')
def index():
    return render_template('aitool.html')

@app.route('/ask_question', methods=['POST'])
def ask_question():
    user_input = request.form.get('user_input')
    response = llm.invoke(user_input)
    return jsonify({'response': response['choices'][0]['text']})

if __name__ == '__main__':
    app.run(debug=True)
