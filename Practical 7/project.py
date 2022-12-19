"""
Practical 7
NGUYEN TAN ANH - JC950881
"""
import datetime

COMPLETION_PERCENTAGE = 100


class ProjectManagement:
    def __init__(self, number, name, start_date, priority, cost_estimate, completion_percentage):
        self.number = number
        self.name = name
        self.start_date = date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        return self.priority <= other.priority

    def is_finished(self):
        return int(self.completion_percentage) == 100

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, " \
               f"completion: {self.completion_percentage}% "

    def compare_date(self, input_date):
        return self.start_date > input_date

    def update_data(self, parameter, value):