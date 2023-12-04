class Project:
    def __init__(self, name, start_date, priority, estimate, completion, completed):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion
        self.completed = completed

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%"
