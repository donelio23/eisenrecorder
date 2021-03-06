import utils.helper as he
import numpy as np


def volume(session, exercise):
    assert exercise in session["exercise list"]
    
    ex = he.get_exercise(session, exercise)
    ex = ex[0]
    
    assert len(ex) == 4 or len(ex) == 3
    
    return vol(ex) 
    
    
def vol(ex): 
    assert len(ex) == 4 or len(ex) == 3
    
    if len(ex) == 4:
       return ex[1]*ex[2]*ex[3]
    else:
       return np.dot(ex[1], ex[2])
    
    
def max_weight(session, exercise):
    assert exercise in session["exercise list"]
    
    ex = he.get_exercise(session, exercise)
    ex = ex[0]
    
    assert len(ex) == 4 or len(ex) == 3
    
    return max_w(ex)


def max_w(exercise):
    assert len(exercise) == 4 or len(exercise) == 3
    
    if len(exercise) == 4:
        return exercise[3]
    
    else:
        return max(exercise[2])
    
    
def reps_max_weight(exercise):
    assert len(exercise) == 4 or len(exercise) == 3
    
    if len(exercise) == 4:
        return exercise[2]
    
    else:
        weights = exercise[2]
        reps = exercise[1]
        
        pos = weights.index(max(weights))
        
        return reps[pos]
    
  
def estimate_onerm(reps, weight):
    percentage = np.array([100, 96, 92, 89, 86, 84, 81, 79, 76, 74])
    percentage = 0.01*percentage
    estimate = weight/percentage[reps-1]
    return round(estimate, 2)