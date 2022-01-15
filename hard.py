"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: This challenge is EXTREMELY hard and we are not expecting anyone to pass all
our tests. In fact, we are not expecting many people to even attempt this.
For complete transparency, this is worth more than the easy challenge. 
A good solution is favourable but does not guarantee a spot in Projects because
we will also consider many other criteria.
"""
import json, re

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()

def is_unlocked(courses_list, target_course):
    # print(CONDITIONS)
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """
    conditions = CONDITIONS[target_course]
    if not courses_list:
        return target_course == "COMP1511"
    if conditions[0] == 'P' or conditions[0] == 'p':
        conditions = conditions.split(None, 1)[1]
    prereqs, req_credits = parser(conditions)
    credits = 6*len(courses_list)
    # print(prereqs, courses_list)
    counter = 0
    for x in courses_list:
        if x in prereqs: 
            counter+=1
    if counter > 0 and (credits >= req_credits):
        return True
    return False

def parser(condition):
    '''
    input: str
    output: list of strings, int
    '''
    prereqs = []
    req_credits = 0
    if condition:
        # subconditons = (re.findall('\(.*?\)', condition))
        # print(subconditons)
        condition = condition.replace("or", "OR")
        condition = condition.replace("and", "AND")
        conditions = condition.split("OR")
        # conditions = [x.split("AND") for x in conditions]
        prereqs = [x.strip() for x in conditions]
    return prereqs, req_credits

    # "COMP2111": "MATH1081 AND    (COMP1511 OR DPST1091 OR COMP1917 OR COMP1921)",
    # "COMP2121": "COMP1917 OR COMP1921 OR COMP1511 OR DPST1091 OR COMP1521 OR DPST1092 OR (COMP1911 AND MTRN2500)",
    
# print(is_unlocked([], "COMP2111"))
# assert(is_unlocked([], "COMP1511") == True)
# assert(is_unlocked(["COMP1511", "COMP1521"], "COMP3151") == False)
# assert(is_unlocked(["COMP1511", "COMP1531"], "COMP2041") == True) 
# assert(is_unlocked([ "COMP1511"], "COMP3161") == False)
# assert(is_unlocked([ "COMP3901"], "COMP3902") == False)

    