"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data(FILENAME)
    print(data)
    for class_data in data:
        print(f'{class_data[0]} is taught by {class_data[1]} and has {class_data[2]} students')


def get_data(filename):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    input_data = processing_data(input_file)
    input_file.close()
    return input_data


def processing_data(input_file):
    processed_data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        processed_data.append(parts)
    return processed_data


main()
