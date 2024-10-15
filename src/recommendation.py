def generate_recommendation(learning_style, performance):
    # Learning style recommendations
    style_recommendations = {
        "Visual": "Use visual aids like diagrams, charts, and videos.",
        "Auditory": "Listen to lectures, podcasts, and engage in discussions.",
        "Kinesthetic": "Engage in hands-on activities, experiments, and practical examples."
    }
    
    weak_subjects = [subject for subject, score in performance.items() if score < 60]
    if weak_subjects:
        advice = f"Focus on improving your performance in {', '.join(weak_subjects)}."
    else:
        advice = "Great work! Keep maintaining balanced progress."

    # Return combined recommendation
    return f"{style_recommendations.get(learning_style, 'Balanced study methods')}\n{advice}"
