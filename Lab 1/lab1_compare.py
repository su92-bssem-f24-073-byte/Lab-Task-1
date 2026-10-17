def rule_based(score, documents_complete):
    if documents_complete and score >= 70:
        return "Review"
    else:
        return "Hold"


# Probability-Based example
def probability_based(probability):
    if probability >= 0.70:
        return "Review"
    else:
        return "Hold"


print("Rule-Based:", rule_based(76, True))
print("Probability-Based:", probability_based(0.76))
