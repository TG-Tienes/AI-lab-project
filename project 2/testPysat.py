# # import tkinter as tk

# # def main():
    
# # the standard way to import PySAT:
from pysat.formula import CNF
from pysat.solvers import Solver, Glucose3

# # create a satisfiable CNF formula "(-x1 ∨ x2) ∧ (-x1 ∨ -x2)":
# cnf = CNF(from_clauses=[[-1 , 2 , 3], [-1 , -1], [3 , -1], [-1 , -1 , -1]])

# cnf = CNF(from_clauses=[[-1,2], [-1,-1], [-1,-1], [2,-1]])


# # create a SAT solver for this formula:
# with Solver(bootstrap_with=cnf) as solver:
#     # 1.1 call the solver for this formula:
#     print('formula is', f'{"s" if solver.solve() else "uns"}atisfiable')

#     # 1.2 the formula is satisfiable and so has a model:
#     print('and the model is:', solver.get_model())

#     # 2.1 apply the MiniSat-like assumption interface:
#     print('formula is',
#         f'{"s" if solver.solve(assumptions=[1, 2]) else "uns"}atisfiable',
#         'assuming x1 and x2')

#     # 2.2 the formula is unsatisfiable,
#     # i.e. an unsatisfiable core can be extracted:
#     print('and the unsatisfiable core is:', solver.get_core())

test = Glucose3()

U = list()
for i in range(2,5):
    U.append(i)





test.add_clause([-1 , 2 , 3])
test.add_clause([-1 , -1])
test.add_clause([3 , -1])
test.add_clause([-1 , -1 , -1])
test.add_clause([int(i) for i in U])

# test.add_clause([1 , -2 , -3])
# test.add_clause([1 , 1])
# test.add_clause([-3 , 1])
# test.add_clause([1 , 1 , 1])

####
# test.add_clause([-1,2])
# test.add_clause([-1,-1])
# test.add_clause([-1,-1])
# test.add_clause([2,-1])


# test.add_clause([1,2,0])
# test.add_clause([-1,3,0])
# test.add_clause([2,3,0])

test.solve()
# print(test.get_model())

modedl = test.get_model()
print(modedl)

# for i in modedl:
#     print(i)