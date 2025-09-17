from collections import Counter
import matplotlib.pyplot as plt

def generate_pie_chart(results, chart_path="bloom_chart.png"):
    levels = [r['bloom_level'] for r in results]
    counts = Counter(levels)
    labels = list(counts.keys())
    sizes = list(counts.values())

    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Bloom Level Distribution")
    plt.savefig(chart_path)
    plt.close()
    return chart_path
