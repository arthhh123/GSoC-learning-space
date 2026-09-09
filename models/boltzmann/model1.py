#import dependencies

import mesa
import seaborn as sns
import numpy as np
import pandas as pd


class MoneyAgent(mesa.Agent):

    def __init__(self, model):
        super().__init__(model)
        self.wealth = 1

    def say_hi(self):
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id
        print(f"Hi, I am an agent, you can call me {self.unique_id!s}.")

    def say_wealth(self):
        print(f"Im an agent with id {self.unique_id!s} and wealth {self.wealth!s}.")

class MoneyModel(mesa.Model):
    """A model with some number of agents."""
    def __init__(self, n=10, rng=None,):
        super().__init__(rng=rng)
        self.num_agents = n
        #create agent
        MoneyAgent.create_agents(model=self, n=n)
    def step(self):
        # This function pseudo-randomly reorders the list of agent objects
        # then iterates through calling the function passed in as the parameter
        self.agents.shuffle_do("say_wealth")


starter_model = MoneyModel(12)
starter_model.step()

        
        