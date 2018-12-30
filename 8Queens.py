import random
import numpy


cross_rate = 1
mutatation_rate = 0.005


def create_community(number_of_solutions,n):
    #N tedad queen ha mibashad
    community = []
    for i in range (number_of_solutions):
        community.append(random.sample(range(n), n))
    return community    

def create_children(parents):
    myChildren = []
    for i in range(0,len(parents)-2,3):
        if probabalistic_decision(cross_rate):
            myChildren.extend(create_kid(parents[i:i+3]))
        else:    
            myChildren.extend(parents[i:i+3])
    return myChildren


def change(solution):
    
    newsolution = solution[:]
    i=0
    j=0
    while i==j:
        i = random.randint(0,len(solution)-1)
        j = random.randint(0,len(solution)-1)
    temp1 = newsolution[j]
    temp2 = newsolution[i]
    newsolution[i] = temp1
    newsolution[j] = temp2
    return newsolution    

def get_fit(solution):
    score = (len(solution)-1)*len(solution)
    for i in range(0,len(solution)):
        for j in range(0,len(solution)):
            if i!=j:
                if i-solution[i] == j-solution[j] or i+solution[i] == j+solution[j]:
                    score-=1
    return score/2            
    
def create_cross(solution1,solution2):
    n = int(len(solution1)/2)
    newsolution1 = solution1[:n] + solution2[n:]
    newsolution2 = solution1[n:] + solution2[:n]
    return (newsolution1,newsolution2)

def probabalistic_decision(probability):
	return random.random() < probability

def create_kid(parents):
    children = parents
    adapt = [get_fit(each_sol) for each_sol in children]
    children.pop(adapt.index(min(adapt)))
    newchild = change(children[random.randint(0, 1)])
    children.append(newchild)
    return(children) 

def runmyGA():

    num_solutions = 24
    n_queens = 8
    generation_limit = 100

    solutions = create_community(num_solutions,n_queens)
    sol_adapt = [get_fit(each_solution) for each_solution in solutions]
    j = 0
    break_flag = False
    while j < generation_limit:
        for i in range(len(sol_adapt)):
            if sol_adapt[i] == n_queens*(n_queens-1)/2:
                print(solutions[i])
                break_flag = True
                break
        else:
            print('Generation {}: Max adapt {}: Sum adapt {}'.format(j,max(sol_adapt),sum(sol_adapt)))
            j+=1
        if break_flag:
            break
        probability_matrix = [x/sum(sol_adapt) for x in sol_adapt]
        ns = numpy.random.choice([i for i in range(num_solutions)],size = num_solutions,p = probability_matrix)
        parents = [solutions[i] for i in ns]
        solutions = parents
        solutions = create_children(parents)
        sol_adapt = [get_fit(each_solution) for each_solution in solutions]
        
        
runmyGA()

