"""
time estimate: 1 hours
start time: 4:23 pm
end time: 6 am morning
"""
import csv
import datetime
from project import ProjectManagement


def main():
    data = []
    print("""
    - (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit""")
    data = load_file('projects.txt')
    projects = add_object(data)
    choice = input('>>>').upper()
    while choice != 'Q':
        if choice == 'L':
            filename = input('Filename: ')
            if filename != '':
                data = load_file(filename)
                projects = add_object(data)
        elif choice == 'S':
            save_filename = input('Please enter the saved file')
            save_file(data, save_filename)
        elif choice == "D":
            complete_project, incomplete_project = group_completeproject(projects)
            print('Incomplete projects: ')
            display_project(incomplete_project)
            print('Completed projects')
            display_project(complete_project)
        elif choice == 'F':
            date_string = input('Show projects that start after date (dd/mm/yy): ')
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filtered_project = []
            for project in projects:
                if project.compare_date(date):
                    filtered_project.append(project)
            display_project(projects)
        elif choice == "A":
            print('Lets add a new project')
            name = input('Name:')
            start_date = input('Start date (dd/mm/yy): ')
            priority = int(input('Priority:'))
            cost_estimate = input('Cost estimate:')
            cost_estimate.replace('$', '')
            cost_estimate = int(cost_estimate)
            percent_complete = input('Percent complete: ')
            project = ProjectManagement(name, start_date, priority, cost_estimate, percent_complete)
            projects.append(project)
        elif choice == 'U':
            display_project(projects)
            project_data = {}
            for number, object in enumerate(projects):
                project_data[number] = object
            project_choice = input('Project choice: ')
            print(project_data[project_choice])
            new_percentage = int(input('New Percentage: '))
            new_priority = int(input('New Priority: '))



def display_project(projects):
    for project in projects:
        print(project)


def group_completeproject(projects):
    """split the project into completed and incomplete projects"""
    completed_project = []
    incomplete_project = []
    for project in projects:
        if project.is_finished():
            completed_project.append(project)
            completed_project.sort()
        else:
            incomplete_project.append(project)
            incomplete_project.sort()
    return completed_project, incomplete_project


def load_file(filename):
    """load the file data to a list of row"""
    in_file = open(filename, 'r')
    data = in_file.readlines()
    projects = csv.reader(data)
    return projects


def save_file(data, filename):
    """save the data to the file as csv mode"""
    out_file = open(filename, 'r')
    print('Name	Start Date Priority	Cost Estimate	Completion Percentage', file=out_file)
    for line in data:
        line = ','.join(line)
        print(line, file=out_file)


def add_object(data):
    projects = []
    for number, line in enumerate(data):
        project = ProjectManagement(number, line[0], line[1], line[2], line[3], line[4])
        projects.append(project)
    return projects





