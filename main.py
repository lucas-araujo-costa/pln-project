from flask import Flask, request, render_template
from document_loader import load_document
from text_processing import correct_spelling, summarize_text
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        file_path = f.filename
        f.save(file_path)
        
        text = load_document(file_path)
        corrected_text = correct_spelling(text)
        summary = summarize_text(corrected_text)
        
        return render_template('results.html', summary=summary, corrected_text=corrected_text)

if __name__ == '__main__':
    app.run(debug=True)
