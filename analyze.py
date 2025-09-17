import sys
from modules.pdf_reader import extract_questions
from modules.bloom_classifier import classify_question
from modules.chart_generator import generate_pie_chart
from modules.correlation import correlate_scores
from modules.report_generator import generate_report

def main(pdf_input, pdf_output):
    questions = extract_questions(pdf_input)
    results = []
    for q in questions:
        analysis = classify_question(q)
        analysis['question'] = q
        results.append(analysis)

    chart_path = generate_pie_chart(results)

    score_map = {
        "Remember": 65,
        "Understand": 72,
        "Apply": 80,
        "Analyze": 85,
        "Evaluate": 78,
        "Create": 90
    }

    correlation_data, overall_score = correlate_scores(results, score_map)
    generate_report(results, chart_path, correlation_data, overall_score, pdf_output)
    print(f"✅ Report saved to: {pdf_output}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
