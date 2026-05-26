def optimize(state):
    return {
        "frequency": "Adaptive",
        "bandwidth": max(10, state['traffic_load'])
    }
