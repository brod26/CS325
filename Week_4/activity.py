# Bryan Rodriguez-Andrade
# CS 325 F2020
# Homework 4, Problem 4


# the base code for the greedy algorithm below was reference from geeks for geeks at https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
def MaxActivities(array):
    jobs = []
    for j in range(len(array)):
        if len(jobs) == 0: # makes sure to always take the job with the latest start time
            jobs.append(array[0])
        elif array[j][2] <= jobs[-1][1]: # greedy step continues to take the job with the latest start time that fits the constraint
            jobs.append(array[j])
    jobs_taken = [job[0] for job in jobs]
    jobs_taken.reverse()
    return(jobs_taken)

# helper function for outputting to the terminal
def output(case, array):
    n = len(array)
    print("Set %d" % (case))
    print("Number of activites selected = %d" % n)
    print("Activites:", *array)

with open('act.txt', 'r') as infile:
    case = 1
    jobs = []
    number_of_jobs = infile.readline().strip()
    # parses data from act.txt into one array of arrays and passes it to the greedy algorithm
    # greedy algorithm returns an array of selected jobs and passes it to the helper function
    # helper function outputs to the terminal, loop continues until the end of the file
    while number_of_jobs != "":
        for job in range(int(number_of_jobs)):
            j, s, f = map(int, infile.readline().strip().split())
            jobs.append([j, s, f])
        jobs.sort(key=lambda x: x[2], reverse=True)
        jobs_taken = MaxActivities(jobs)
        output(case, jobs_taken)
        case += 1
        jobs = []
        number_of_jobs = infile.readline().strip()