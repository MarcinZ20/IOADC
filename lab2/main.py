import time

from searchBranchAndBound import DF_branch_and_bound
from searchMPP import SearcherMPP
from stripsProblem import *
from stripsRegressionPlanner import Regression_STRIPS


def custom_heur_1(state, goal):
    heur_value = 0
    for s, v in state.items():
        for s_g, v_g in goal.items():
            if s == s_g:
                heur_value += not v == v_g

    return heur_value

blocks1domain = create_blocks_world({'a', 'b', 'c', 'd', 'e', 'f'})
blocks2domain = create_blocks_world({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'})
blocks3domain = create_blocks_world({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'})

problem1 = Planning_problem(blocks1domain,
                            {on('a'): 'table', clear('a'): True,
                             on('b'): 'table', clear('b'): True,
                             on('c'): 'table', clear('c'): True,
                             on('d'): 'table', clear('d'): True,
                             on('e'): 'table', clear('e'): True,
                             on('f'): 'table', clear('f'): True},  # initial state
                            {clear('a'): True, on('a'): 'b',
                             clear('b'): False, on('b'): 'c',
                             clear('c'): False, on('c'): 'd',
                             clear('d'): False, on('d'): 'table'}, )  # goal

sub_goal_1_1 = {clear('f'): True, on('f'): 'table'}
sub_goal_1_2 = {clear('e'): True, on('e'): 'table'}

problem2 = Planning_problem(blocks1domain,
                            {on('a'): 'table', clear('a'): True,
                             on('b'): 'table', clear('b'): True,
                             on('c'): 'table', clear('c'): True,
                             on('d'): 'table', clear('d'): True,
                             on('e'): 'table', clear('e'): True,
                             on('f'): 'table', clear('f'): True},  # initial state
                            {clear('a'): True, on('a'): 'b',
                             clear('b'): False, on('b'): 'c',
                             clear('d'): True, on('d'): 'e',
                             clear('e'): False, on('e'): 'f'})  # goal

sub_goal_2_1 = {clear('d'): True, on('d'): 'table'}
sub_goal_2_2 = {clear('c'): True, on('c'): 'table'}

problem3 = Planning_problem(blocks2domain,
                            {on('a'): 'table', clear('a'): True,
                             on('b'): 'table', clear('b'): True,
                             on('c'): 'table', clear('c'): True,
                             on('d'): 'table', clear('d'): True,
                             on('e'): 'table', clear('e'): True,
                             on('f'): 'table', clear('f'): True,
                             on('g'): 'table', clear('g'): True,
                             on('h'): 'table', clear('h'): True,
                             on('i'): 'table', clear('i'): True},  # initial state
                            {clear('a'): True, on('a'): 'table',
                             clear('b'): False, on('b'): 'table',
                             clear('c'): True, on('c'): 'b',
                             clear('d'): False, on('d'): 'table',
                             clear('e'): False, on('e'): 'd',
                             clear('f'): True, on('f'): 'e',
                             clear('g'): False, on('g'): 'table',
                             clear('h'): True, on('h'): 'g',
                             clear('i'): True, on('i'): 'table'})  # goal

sub_goal_3_1 = {clear('i'): True, on('i'): 'table'}
sub_goal_3_2 = {clear('h'): True, on('g'): 'table'}

print("Length:", len(problem1.initial_state))

print("======= ======= =======\n\nWith custom heuristic\n\n======= ======= =======\n\n")
timeStart = time.time()
SearcherMPP(Regression_STRIPS(problem1, heur=custom_heur_1)).search()   #A* with MPP
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
DF_branch_and_bound(Regression_STRIPS(problem1, custom_heur_1),10).search() #B&B
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
SearcherMPP(Regression_STRIPS(problem2, heur=custom_heur_1)).search()   #A* with MPP
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
DF_branch_and_bound(Regression_STRIPS(problem2, heur=custom_heur_1),10).search() #B&B
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
SearcherMPP(Regression_STRIPS(problem3, heur=custom_heur_1)).search()   #A* with MPP
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
DF_branch_and_bound(Regression_STRIPS(problem3, heur=custom_heur_1),10).search() #B&B
timeStop = time.time()
print("time: ", timeStop - timeStart)



print("===== ===== =====\n\nWithout custom heuristic\n\n===== ===== =====\n\n")
timeStart = time.time()
SearcherMPP(Regression_STRIPS(problem1)).search()   #A* with MPP
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
DF_branch_and_bound(Regression_STRIPS(problem1),10).search() #B&B
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
SearcherMPP(Regression_STRIPS(problem2)).search()   #A* with MPP
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
DF_branch_and_bound(Regression_STRIPS(problem2),10).search() #B&B
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
SearcherMPP(Regression_STRIPS(problem3)).search()   #A* with MPP
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
DF_branch_and_bound(Regression_STRIPS(problem3),10).search() #B&B
timeStop = time.time()
print("time: ", timeStop - timeStart)

# ================= Additional problems =================

initial_state_4 = {on('a'): 'table', clear('a'): True,
                   on('b'): 'table', clear('b'): True,
                   on('c'): 'table', clear('c'): True,
                   on('d'): 'table', clear('d'): True,
                   on('e'): 'table', clear('e'): True,
                   on('f'): 'table', clear('f'): True,
                   on('g'): 'table', clear('g'): True,
                   on('h'): 'table', clear('h'): True,
                   on('i'): 'table', clear('i'): True,
                   on('j'): 'table', clear('j'): True,
                   on('k'): 'table', clear('k'): True,
                   on('l'): 'table', clear('l'): True}

goal_4 = {clear('a'): True, on('a'): 'table',
          clear('b'): False, on('b'): 'table',
          clear('c'): False, on('c'): 'b',
          clear('d'): True, on('d'): 'c',
          clear('e'): False, on('e'): 'd',
          clear('f'): False, on('f'): 'e',
          clear('g'): True, on('g'): 'f',
          clear('h'): True, on('h'): 'g',
          clear('i'): True, on('i'): 'h',
          clear('j'): False, on('j'): 'i',
          clear('k'): False, on('k'): 'j',
          clear('l'): True, on('l'): 'k'}

initial_state_5 = initial_state_4.copy()
initial_state_5.update({on('m'): 'table', clear('m'): True,
                        on('n'): 'table', clear('n'): True,
                        on('o'): 'table', clear('o'): True,
                        on('p'): 'table', clear('p'): True,
                        on('q'): 'table', clear('q'): True,
                        on('r'): 'table', clear('r'): True,
                        on('s'): 'table', clear('s'): True})

goal_5 = {clear('m'): True, on('m'): 'table',
          clear('n'): False, on('n'): 'table',
          clear('o'): True, on('o'): 'n',
          clear('p'): False, on('p'): 'o',
          clear('q'): True, on('q'): 'p',
          clear('r'): False, on('r'): 'q',
          clear('s'): True, on('s'): 'r'}

initial_state_6 = initial_state_5.copy()
initial_state_6.update({clear('t'): True, on('t'): 'table',
                        clear('u'): True, on('u'): 'table',
                        clear('v'): True, on('v'): 'table',
                        clear('w'): True, on('w'): 'table',
                        clear('x'): True, on('x'): 'table',
                        clear('y'): True, on('y'): 'table',
                        clear('z'): True, on('z'): 'table'})

goal_6 = {clear('t'): False, on('t'): 's',
          clear('u'): False, on('u'): 't',
          clear('v'): False, on('v'): 'u',
          clear('w'): False, on('w'): 'v',
          clear('x'): False, on('x'): 'w',
          clear('y'): False, on('y'): 'x',
          clear('z'): True, on('z'): 'y'}

problem4 = Planning_problem(blocks2domain, initial_state_4, goal_4)
problem5 = Planning_problem(blocks2domain, initial_state_5, goal_5)
problem6 = Planning_problem(blocks2domain, initial_state_6, goal_6)

print("Number of actions in Problem 4:", len(problem4.domain.actions))
print("Number of actions in Problem 5:", len(problem5.domain.actions))
print("Number of actions in Problem 6:", len(problem6.domain.actions))

print("======= ======= =======\n\nWith custom heuristic\n\n======= ======= =======\n\n")
timeStart = time.time()
SearcherMPP(Regression_STRIPS(problem4, heur=custom_heur_1)).search()   #A* with MPP
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
DF_branch_and_bound(Regression_STRIPS(problem4, heur=custom_heur_1),10).search() #B&B
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
SearcherMPP(Regression_STRIPS(problem5, heur=custom_heur_1)).search()   #A* with MPP
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
DF_branch_and_bound(Regression_STRIPS(problem5, heur=custom_heur_1),10).search() #B&B
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
SearcherMPP(Regression_STRIPS(problem6, heur=custom_heur_1)).search()   #A* with MPP
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
DF_branch_and_bound(Regression_STRIPS(problem6, heur=custom_heur_1),10).search() #B&B
timeStop = time.time()
print("time: ", timeStop - timeStart)

print("===== ===== =====\n\nWithout custom heuristic\n\n===== ===== =====\n\n")
timeStart = time.time()
SearcherMPP(Regression_STRIPS(problem4)).search()   #A* with MPP
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
DF_branch_and_bound(Regression_STRIPS(problem4),10).search() #B&B
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
SearcherMPP(Regression_STRIPS(problem5)).search()   #A* with MPP
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
DF_branch_and_bound(Regression_STRIPS(problem5),10).search() #B&B
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
SearcherMPP(Regression_STRIPS(problem6)).search()   #A* with MPP
timeStop = time.time()
print("time: ", timeStop - timeStart)

timeStart = time.time()
DF_branch_and_bound(Regression_STRIPS(problem6),10).search() #B&B
timeStop = time.time()
print("time: ", timeStop - timeStart)
