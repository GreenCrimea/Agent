import random
from calculate_action import CalculateAction

def UpdateMap(agents, environment, config, metadata, score):

 for i in range(config['population']):
  metadata, environment, score = CalculateAction(agents, environment, config, metadata, i, score)

 return metadata, environment, score



def DoRun(agents, environment, config, metadata, z):
 score = []
 a = 0
 for i in range(len(agents)):
  score.append(a)

 steps = config['steps']
 for i in range(steps):


  print(f'GEN{z}, STEP{i}___agent 0>{metadata[0][0]}, {metadata[1][0]} | agent 1>{metadata[0][1]}, {metadata[1][1]} | agent 2>{metadata[0][2]}, {metadata[1][2]}')



  metadata, environment, score = UpdateMap(agents, environment, config, metadata, score)


 return metadata, environment, score
