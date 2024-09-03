from flask import Flask, render_template, request, jsonify
import your_nlp_module  # This will be the module where your NLP code resides

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    summary = your_nlp_module.summarize(text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
 