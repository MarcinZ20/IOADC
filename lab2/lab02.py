from stripsForwardPlanner import Forward_STRIPS
from stripsProblem import *
from searchBranchAndBound import DF_branch_and_bound
from searchMPP import SearcherMPP
import stripsProblem

blocks1domain = create_blocks_world({'a', 'b', 'c', 'd', 'e'})
problem1 = Planning_problem(blocks1dom,
                            {on('a'): 'table', clear('a'): True,
                             on('b'): 'table', clear('b'): True,
                             on('c'): 'table', clear('c'): True,
                             on('d'): 'table', clear('d'): True,
                             on('e'): 'table', clear('e'): True},  # initial state
                            {on('b'): 'c', clear('c'): False})  # goal

print("Length:", len(problem1.initial_state))

SearcherMPP(Forward_STRIPS(problem1)).search()  #A* with MPP
DF_branch_and_bound(Forward_STRIPS(problem1),10).search() #B&B
# To find more than one plan:
s1 = SearcherMPP(Forward_STRIPS(problem1))  #A*
s1.search()  #find another plan