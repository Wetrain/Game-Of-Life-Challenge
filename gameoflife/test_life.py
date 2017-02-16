from Life import Life

state = [[0 for r in range(3)] for c in range(3)]

state[1][0] = 1
state[1][1] = 1
state[1][2] = 1

l = Life(state=state, size=3)

l.visual_evolve(2)
