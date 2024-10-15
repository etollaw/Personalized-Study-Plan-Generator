def optimize_learning_path(student):
    if student.performance['math'] < 60:
        return "Focus more on math. Recommended: 2 hours daily with extra practice."
    return "Balanced study schedule."
