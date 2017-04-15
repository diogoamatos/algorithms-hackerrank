# -*- coding: utf-8 -*-
# Grading Students
#
# n = int(raw_input().strip())
# grades = []
# for i in range(n):
#     grades.append(int(raw_input()))
#
#
# rounded_grades = []
#
# for i in range(n):
#     max_grade = 100
#     while max_grade >= 40:
#         if max_grade > grades[i] and max_grade - grades[i] < 3:
#             grades[i] = max_grade
#         max_grade -= 5
#
# for i in range(n):
#     print grades[i]
#

# !/bin/python

import sys


def solve(grades):
    # Complete this function
    for i in range(len(grades)):
        max_grade = 100
        while max_grade >= 40 and grades[i] > 35:
            if max_grade > grades[i] and max_grade - grades[i] < 3:
                grades[i] = max_grade
            max_grade -= 5

    return grades


n = int(raw_input().strip())

grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)

for i in result:
    print i
