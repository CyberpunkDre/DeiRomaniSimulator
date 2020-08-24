'''

minerva.py

This object's role in the simulation is to hold models.
It will coordinate with Janus to step through the simulated models.

Assume models are outside Python objects with following attributes/methods/API
'''

class Model(object):

    def __init__(self, behavior_profile):
        self.current_data = 0
        self.behavior_profile = behavior_profile
    
    def compute(self, time, input_data):
        output_data = 0
        return output_data

    def write_row(self):
        return [current_data]

class Minerva(object):

    def __init__(self, ordered_model_list):
        self.models = ordered_model_list
        print("Minerva Online.")

    def step(self, time):
        pass_through_data = None
        return_data = None
        for model in self.models:
            return_data = model.compute(time, pass_through_data)

    def get_record(self):
        model_records = []
        for model in self.models:
            model_records.append(model.write_row())
        return model_records
        
def main():
    print("You are in a maze of twisty little passages, all alike")

if __name__ == "__main__":
    main()