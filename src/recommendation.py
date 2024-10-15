def generate_recommendation(student):
    recommendations = {
        "Visual": "Use mind maps, diagrams, and videos.",
        "Auditory": "Listen to podcasts, record notes, and participate in discussions.",
        "Kinesthetic": "Use hands-on activities, experiments, and role-playing."
    }
    return recommendations.get(student.learning_style, "General study advice.")
