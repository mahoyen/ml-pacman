
class QConfig(object):
    def __init__(self):
        self.discount = 0.8
        self.alpha = 0.2


class DeepQConfig(object):
    def __init__(self):
        self.num_actions = 4
        self.input_size = 60
        self.hidden_size = 512
