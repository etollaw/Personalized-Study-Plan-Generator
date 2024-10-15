from recommendation import generate_recommendation
from ai_optimizer import optimize_learning_path


class Student:
    def __init__(self, name, learning_style, performance):
        self.name = name
        self.learning_style = learning_style
        self.performance = performance  # e.g., {"math": 85, "science": 75}

    def __repr__(self):
        return f"Student({self.name}, {self.learning_style}, {self.performance})"

student1 = Student("Alex", "Visual", {"math": 50, "science": 80})

print(f"Recommendations: {generate_recommendation(student1)}")
print(f"Learning Path Optimization: {optimize_learning_path(student1)}")
