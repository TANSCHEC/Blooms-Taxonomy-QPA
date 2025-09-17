from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_report(results, chart_path, correlation_data, overall_score, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Bloom Taxonomy Analysis Report")
    y -= 40

    c.drawImage(chart_path, 50, y - 300, width=400, height=300)
    y -= 320

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Correlation with Student Scores")
    y -= 30
    c.setFont("Helvetica", 12)
    for item in correlation_data:
        line = f"{item['level']}: {item['questions']} questions → Avg Score: {item['avg_score']} → Weighted Score: {item['weighted_score']}"
        c.drawString(50, y, line)
        y -= 20
    c.drawString(50, y, f"Estimated Overall Performance Score: {overall_score}")
    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Question Analysis")
    y -= 30
    c.setFont("Helvetica", 12)
    for idx, item in enumerate(results, 1):
        block = f"{idx}. {item['question']}\n→ Level: {item['bloom_level']}\n→ Reason: {item['reason']}\n→ Suggestion: {item['suggestion']}\n"
        for line in block.split('\n'):
            c.drawString(50, y, line)
            y -= 20
            if y < 100:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 12)
    c.save()
