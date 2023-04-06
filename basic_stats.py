Author: Justin Huang
# GitHub username: huangjus
# Date: 4/5/23
# Description: This function is designed to calculate and return the mean, median, and mode of scores from a list of
# student objects. The function takes a list of student objects as input, where each student object has a name
# and a score. The function then extracts the scores from each student object and calculates the mean, median,
# and mode of the scores. Finally, the function returns these three statistical measures as a tuple.

import statistics

class Student:
    """
    A class representing a student with a name and grade.
    """

    def __init__(self, name, grade):
        """
        Initialize the Student object with a name and grade.
        """

        self.__name = name
        self.__grade = grade

    def get_grade(self):
        """
        Get the student's grade.
        """

        return self.__grade

def basic_stats(student_list):
    """
    Calculate the mean, median, and mode of the grades from a list of Student objects.
    """

    grades = [student.get_grade() for student in student_list]

    mean_grade = statistics.mean(grades)
    median_grade = statistics.median(grades)
    mode_grade = statistics.mode(grades)

    return mean_grade, median_grade, mode_grade
