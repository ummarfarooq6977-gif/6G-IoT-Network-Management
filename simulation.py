import random
def generate_state():
    return {
        "population_density": random.randint(100,1000),
        "traffic_load": random.uniform(0,100),
        "latency": random.uniform(1,50)
    }
