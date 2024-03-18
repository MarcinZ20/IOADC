from lab2.aipython.stripsHeuristic import h1
from stripsForwardPlanner import Forward_STRIPS
from stripsProblem import *
from searchBranchAndBound import DF_branch_and_bound
from searchMPP import SearcherMPP
import stripsProblem
import time


def custom_heur_1(state, goal):
 heur_value = 0
 for s, v in state.items():
  for s_g, v_g in goal.items():
   if s == s_g:
    heur_value += not v == v_g
 # print("State:", state)
 # print("Goal:", goal)
 # print("Heurisitc:", heur_value)
 return heur_value

blocks1domain = create_blocks_world({'a', 'b', 'c', 'd', 'e', 'f'})
blocks2domain = create_blocks_world({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'})
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
                             clear('d'): False, on('d'): 'table'})  # goal

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

print("Length:", len(problem1.initial_state))
#
# SearcherMPP(Forward_STRIPS(problem1)).search()  #A* with MPP
# DF_branch_and_bound(Forward_STRIPS(problem1),10).search() #B&B
# # To find more than one plan:
# s1 = SearcherMPP(Forward_STRIPS(problem1))  #A*
# s1.search()  #find another plan

from lab2.aipython.stripsRegressionPlanner import Regression_STRIPS
from searchBranchAndBound import DF_branch_and_bound
from searchMPP import SearcherMPP
import stripsProblem

print("\n\nwith custom heuristic\n\n")
timeStart = time.time()

SearcherMPP(Regression_STRIPS(problem1, heur=custom_heur_1)).search()   #A* with MPP
# DF_branch_and_bound(Regression_STRIPS(problem1),10).search() #B&B
#
SearcherMPP(Regression_STRIPS(problem2, heur=custom_heur_1)).search()   #A* with MPP
# DF_branch_and_bound(Regression_STRIPS(problem2),10).search() #B&B
#
SearcherMPP(Regression_STRIPS(problem3, heur=custom_heur_1)).search()   #A* with MPP
# DF_branch_and_bound(Regression_STRIPS(problem3),10).search() #B&B

timeStop = time.time()

print("time: ", timeStop - timeStart)



print("\n\nwithout custom heuristic\n\n")
timeStart = time.time()
SearcherMPP(Regression_STRIPS(problem1)).search()   #A* with MPP
# DF_branch_and_bound(Regression_STRIPS(problem1),10).search() #B&B
#
SearcherMPP(Regression_STRIPS(problem2)).search()   #A* with MPP
# DF_branch_and_bound(Regression_STRIPS(problem2),10).search() #B&B
#
SearcherMPP(Regression_STRIPS(problem3)).search()   #A* with MPP
# DF_branch_and_bound(Regression_STRIPS(problem3),10).search() #B&B
timeStop = time.time()
print("time: ", timeStop - timeStart)

