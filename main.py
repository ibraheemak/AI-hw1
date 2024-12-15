import time
from IPython.display import clear_output

from typing import List, Tuple
from HaifaEnv import HaifaEnv
from Algorithms import *

DOWN = 0
RIGHT = 1
UP = 2
LEFT = 3

MAPS = {
    "4x4": ["SFFF",
            "FHFH",
            "FFFH",
            "HFFG"],
    "8x8": ["SFFFFFFF",
            "FFFFFTAL",
            "TFFHFFTF",
            "FPFFFHTF",
            "FAFHFPFF",
            "FHHFFFHF",
            "FHTFHFTL",
            "FLFHFFFG"],
    "5x5": ["SFFFG",
            "PHHHH",
            "PHHHH",
            "GHHHH",
            "HHHHH"],
}



def print_solution(actions,env: HaifaEnv) -> None:
    env.reset()
    total_cost = 0
    print(env.render())
    print(f"Timestep: {1}")
    print(f"State: {env.get_state()}")
    print(f"Action: {None}")
    print(f"Cost: {0}")
    time.sleep(1)

    for i, action in enumerate(actions):
      state, cost, terminated = env.step(action)
      total_cost += cost
      clear_output(wait=True)

      print(env.render())
      print(f"Timestep: {i + 2}")
      print(f"State: {state}")
      print(f"Action: {action}")
      print(f"Cost: {cost}")
      print(f"Total cost: {total_cost}")

      time.sleep(1)

      if terminated is True:
        break

env = HaifaEnv(MAPS["5x5"])
state = env.reset()
print('Initial state:', state)
print('Goal states:', env.goals)


BFSG_agent = BFSGAgent()
actions, total_cost, expanded = BFSG_agent.search(env)
print(f"Total_cost: {total_cost}")
print(f"Expanded: {expanded}")
print(f"Actions: {actions}")
print_solution(actions, env)
#assert total_cost == 164.0, "Error in total cost returned"
#assert expanded == 55, "Error in number of expanded nodes returned"