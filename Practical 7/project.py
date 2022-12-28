"""
Practical 7
NGUYEN TAN ANH - JC950881
estimate time: 6 hours
complete time: 4 hours
"""
import datetime

COMPLETION_PERCENTAGE = 100


class ProjectManagement:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """
        initialise parameter for project objects
        :param name: name of the project
        :param start_date: start date of the project
        :param priority: priority point of the project
        :param cost_estimate: estimate cost of the project
        :param completion_percentage: completion percentage of the project
        """
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __lt__(self, other):
        """sort the project by priority for incomplete, complete projects display"""
        return self.priority <= other.priority

    def is_finished(self):
        """check if the project is finished by completion percentage is 100%"""
        return int(self.completion_percentage) == 100

    def __str__(self):
        """display project data"""
        start_date = self.start_date.strftime("%d/%m/%Y")
        return f" {self.name}, start: {start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, " \
               f"completion: {self.completion_percentage}% "

    def compare_date(self, input_date):
        """compare the input date with project start date"""
        input_date = datetime.datetime.strptime(input_date, "%d/%m/%Y").date()
        return self.start_date >= input_date

    def update_percentage(self, value):
        """change the project complete percentage"""
        self.completion_percentage = value

    def update_priority(self, value):
        """change the project priority point"""
        self.priority = value
