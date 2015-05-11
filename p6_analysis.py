from p6_game import Simulator
from math import sqrt
from collections import deque

ANALYSIS = {}

def analyze(design):


    visited = {}
    prev = {}
    queve = deque()
    # visited = []
    sim = Simulator(design)
    init = sim.get_initial_state()
    init_pos, init_ability = init

    ANALYSIS[init_pos] = None
    # print ANALYSIS[init_pos]

    visited[init_pos] = init_ability
    queve.append(init)
    # # while queve is not empty 
    while queve:

        current_state = queve.popleft()
        current_position,current_abilities = current_state


    #     # if node has reached its destination cell it will quit while loop
    #     # calls the get_steps function stored in adj
        moves = sim.get_moves()
        for next_move in moves:
            if next_move == "NOTHING":
                continue

            next_state = sim.get_next_state(current_state,next_move)
            if next_state == None:
                # ANALYSIS[next_position] = None 
                continue
            # if in the current state the character dies ignore this state
            

            next_position, next_abilities = next_state
           

            if next_position == current_position:
                continue

            # stores new ability into Analysis for later use when it comes to drawing out the lines
            if next_position not in visited:
                visited[next_position] = current_abilities
                ANALYSIS[next_position] = current_position
                queve.append(next_state)
            elif next_position in visited:
                for ability in next_abilities:
                    if ability not in visited[next_position]:
                        visited[next_position] = current_abilities
                        # ANALYSIS[next_position] = current_position
                        queve.append(next_state)


           
            # elif next_position in visited:
            #     ANALYSIS[next_position] = current_position
            #     queve.append(next_state)


            # elif next_position in visited:
            #     ANALYSIS[next_position] = current_position
            #     queve.append(next_state)
                

              
       
    # ANALYSIS.reverse()
    print current_abilities
# returns true if the path has been visited with the current abilities 
# returns false otherwise
def visited_with(current_abilities, visited):
    for ability in current_abilities:
        print ability

    


    # TODO: fill in this function, populating the ANALYSIS dict
# checks if the current state can traverse the next state, checks
# what current abilitoes the state has and what are requred to move
# to the next state. if 

def distance(current_state, next_state,sim):
    current_position,current_abilities = current_state
    next_position,next_abilities = next_state

    xA,yA = current_position
    xB,yB = next_position
    return (sqrt(pow((xB - xA),2) + pow((yB - yA),2)))


def inspect((i,j), draw_line):
    current_position = (i,j)

    while current_position != None and current_position in ANALYSIS :
        next_position = ANALYSIS[current_position]
        if next_position != None:
          draw_line(current_position, next_position,offset_obj = None, color_obj='W')
        current_position = next_position


    # TODO: use ANALYSIS and (i,j) draw some lines
