import numpy as np

from HaifaEnv import HaifaEnv
from typing import List, Tuple
import heapdict


########################################
class Node():
     def __init__(self, state, parent=None, action=None, g=0):
        self.state=state
        self.parent=parent
        self.action=action # the action we did to reach this state
        self.g=g # path cost

########################################     
class  Agent:
  def __init__(self) -> None:
    self.env = None

  def solution(self, node): # the sequence of actions
    actions = []
    while node.parent is not None :
      actions.append(node.action)
      node=node.parent
    actions.reverse()
    return actions
     
########################################  


class BFSGAgent(Agent):

    def __init__(self) -> None:
      super().__init__()
        

    def search(self, env: HaifaEnv) -> Tuple[List[int], float, int]:
      currNode=Node(state=env.get_initial_state(),g=0)
      if env.is_final_state(currNode.state):
        return self.solution(currNode),currNode.g,0
      open=[currNode]
      close=set()
      expanded=0
      
      while open :
        currNode=open.pop(0)
        close.add(currNode.state)
        expanded+=1
        for action, (new_state, step_cost, terminated) in env.succ(currNode.state).items():
          if new_state is None or step_cost is None:
            continue
          child=Node(state=new_state,parent=currNode,action=action,g=currNode.g+step_cost)
          if child.state not in close and all(node.state != new_state for node in open):
            if env.is_final_state(child.state):
               return self.solution(child),child.g,expanded
            open.append(child)

      return [], float("inf"), expanded 


        
########################################
class GreedyAgent():
  
    def __init__(self) -> None:
        raise NotImplementedError

    def search(self, env: HaifaEnv) -> Tuple[List[int], float, int]:
        raise NotImplementedError



class WeightedAStarAgent():
    
    def __init__(self):
        raise NotImplementedError

    def search(self, env: HaifaEnv, h_weight) -> Tuple[List[int], float, int]:
        raise NotImplementedError   



class AStarAgent():
    
    def __init__(self):
        raise NotImplementedError

    def search(self, env: HaifaEnv) -> Tuple[List[int], float, int]:
        raise NotImplementedError 

