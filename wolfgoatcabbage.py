from search import *

class WolfGoatCabbage(Problem):
    #a constructor that sets the initial and goal states
    def __init__(self,initial=frozenset({'G', 'F', 'W', 'C'}),goal=set()):
        super().__init__(initial, goal)         #extend class Problem

    #a method goal_test(state) that returns True if the given state is a goal state
    def goal_test(self,state):
        if state==self.goal:
            return True
        else:
            return False
    
    #a method actions(state) that returns a list of valid actions in the given state
    def actions(self,state): 
        hashmap = {
                    frozenset({'F', 'G', 'W', 'C'}):[{'F','G'}],
                    frozenset({'W', 'C'}):[{'F'}],
                    frozenset({'W', 'C','F'}):[{'W','F'},{'C','F'}],
                    frozenset({'W'}): [{'G','F'}],
                    frozenset({'C'}): [{'G','F'}],
                    frozenset({'G', 'F', 'C'}):[{'C','F'}],
                    frozenset({'G', 'F', 'W'}): [{'W','F'}],
                    frozenset({'G'}): [{'F'}],
                    frozenset({'G', 'F'}): [{'G','F'}]
        
        }
        for i in hashmap:
            if state==i:
                return hashmap[i]


    '''
    a method result(state, action) that returns the new state reached from the given 
    state and the given action. Assume that the action is valid.
    In result() you will have to return the next state as a frozenset since the search 
    algorithms require the state to be represented as a hashable data type.
    '''
    def result(self, state, action):
        nextState = set()
        for i in state:
            nextState.add(i)

        x = [nextState.add(i) if i not in state else nextState.remove(i) for i in action]
        return frozenset(nextState)

if __name__ == '__main__':
    wgc = WolfGoatCabbage(frozenset({'G', 'F', 'W', 'C'}),set())
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
    
#expected output
#[{'G', 'F'}, {'F'}, {'C', 'F'}, {'G', 'F'}, {'W', 'F'}, {'F'}, {'G', 'F'}]
#[{'G', 'F'}, {'F'}, {'W', 'F'}, {'G', 'F'}, {'C', 'F'}, {'F'}, {'G', 'F'}]
