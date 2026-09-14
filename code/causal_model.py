from ylearn.causal_model.graph import CausalGraph
from ylearn.causal_model.graph import CausalModel

causation = (
    'X1':[],
    'X2':[],
    'X3':['X1'],
    'X4':['X1', 'X2'],
    'X5':['X2'],
    'X6':['X', 'X1', 'X2'],
    'X':['X3', 'X4', 'X5'],
    'Y':['X', 'X3', 'X4', 'X5', 'X6'],
) 

cg = CausalGraph(causation=causation)
cm = CausalModel(causal_graph=cg)
backdoor_set, prob = cm.identify(treatment={'X'}, outcome={'Y'}, identify_method=('backdoor', 'simple'))['backdoor']

print(backdoor_set)