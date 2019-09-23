
#from pyaixi import agent, prediction, search, util, environment, environments
from mc_aixi_ctw import MC_AIXI_CTW_Agent
from pyaixi.environment import Environment
from pyaixi.environments.coin_flip import CoinFlip
from pyaixi.agent import update_enum, action_update, percept_update

import pytest

m = 10 # agent horizon
d = 10 # CT depth
s = 10 # number of simulations
env = CoinFlip()

options = {'agent-horizon': m,
           'ct-depth': d,
           'mc-simulations': s}

print("---======== BEGIN TEST ========---")

aixi = MC_AIXI_CTW_Agent(env, options)
percept = aixi.generate_percept_and_update()

#initial percept should always be (0,0) and last update must be percept_update
def initial_percept():
    assert percept == (0,0), "initial percept is not (0,0)"
    assert aixi.last_update == percept_update, "last update is not percept_update"
    print("succesfully recorded initial percept "+str(percept))
initial_percept()

#check if action is in action space
action = aixi.generate_random_action()
def action_is_in_action_space():
    assert action in aixi.environment.valid_actions, "action is not in action space"
    print("succesfully performed valid action "+str(action))
action_is_in_action_space()

#check if action is recorded in environment
aixi.model_update_action(action)
def action_is_recorded_in_env():
    assert action == aixi.environment.action, "environment did not record last action"
    assert aixi.last_update == action_update, "last update is not action_update"
    print("succesfully recorded action "+str(action))
action_is_recorded_in_env()

print("---======== END TEST ========---")

