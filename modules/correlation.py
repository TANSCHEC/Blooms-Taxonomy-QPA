from collections import Counter

def correlate_scores(results, score_map):
    level_counts = Counter([r['bloom_level'] for r in results])
    total = sum(level_counts.values())
    correlation = []

    for level, count in level_counts.items():
        avg_score = score_map.get(level, 0)
        weight = count / total
        correlation.append({
            "level": level,
            "questions": count,
            "avg_score": avg_score,
            "weighted_score": round(avg_score * weight, 2)
        })

    overall = round(sum(c['weighted_score'] for c in correlation), 2)
    return correlation, overall
