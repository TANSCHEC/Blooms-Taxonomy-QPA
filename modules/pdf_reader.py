import re
import PyPDF2

def extract_questions(pdf_path):
    questions = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            for line in text.split('\n'):
                if re.match(r'^\d+\.', line.strip()):
                    questions.append(line.strip())
    return questions
